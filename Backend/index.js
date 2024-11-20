require('dotenv').config();
const express = require('express');
const { spawn } = require('child_process');

// Create an express app
const app = express();

const executePython = async (script, args) => {
    const py = spawn("python", [script, ...args]);

    const result = await new Promise((resolve, reject) => {
        let output = '';
        let errorOutput = '';

        py.stdout.on('data', (data) => {
            output += data.toString();
        });

        py.stderr.on('data', (data) => {
            errorOutput += data.toString();
        });

        py.on('exit', (code) => {
            if (code === 0) {
                try {
                    resolve(JSON.parse(output));
                } catch (err) {
                    reject({ status: "error", message: "Invalid JSON output from script" });
                }
            } else {
                reject({ status: "error", message: errorOutput || "Unknown error occurred" });
            }
        });
    });

    return result;
};

// Middleware
app.use((req, res, next) => {
    console.log(req.method, req.path);
    next();
});

// Routes
app.get('/crawl', async (req, res) => {
    // const seedUrls = req.query.urls ? req.query.urls.split(',') : [];
    const seedUrls = [
        "https://www.cnn.com",
        "https://www.cnn.com/politics/live-news/election-trump-harris-11-08-24/index.html"
    ];
    if (seedUrls.length === 0) {
        return res.status(400).json({ status: "error", message: "No seed URLs provided" });
    }

    try {
        const result = await executePython('crawler.py', seedUrls);
        res.json(result);
    } catch (error) {
        res.status(500).json(error);
    }
});

app.get('/search', async (req, res) => {
    const query = req.query.q;
    if (!query) {
        return res.status(400).json({ status: "error", message: "No query provided" });
    }

    try {
        const result = await executePython('query.py', [query]);
        res.json(result);
    } catch (error) {
        res.status(500).json(error);
    }
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log('Server is listening on port', port);
});