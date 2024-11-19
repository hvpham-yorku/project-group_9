const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.json({msg: 'Hello World'});
});

app.listen(4000, () => {
    console.log('Server is listening on port 4000');
});