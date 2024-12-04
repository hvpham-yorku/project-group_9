# Sprint 2 Planning Document (sprint2.md)

**Date:** November 23, 2024  
**Sprint Duration:** November 21 – December 3, 2024

## Participants
- Jordi Nakahara (Product Owner)
- Harman Goraya (Back End Developer)
- Kashif Syed (Back End Developer)
- Maaz Siddiqui (Front End Developer)

## Sprint Goal
Refine the functionality introduced in sprint 1, add the features that weren't able to be implemented in sprint 1, and add the remaining functionality.

## User Stories for Sprint 1
1. **Story 1:** I want to search for answers to my children’s questions, **so that** I can provide answers quickly and reliably, even if I'm unfamiliar with the topic.
   - **Tasks:** 
     - Research and select crawling libraries
     - Write a script to crawl based on a URL
     - Store crawled data in a structured format
2. **Story 2:** I want AI-powered predictions for common questions, **so that** I can type less and still find relevant results quickly.
   - **Tasks:** 
     - Research AI-powerered predictions
     - Create the functionality in python
     - Use index.js to communicate the results of the prediction to the frontend
3. **Story 3:** I want to see a summary of complex articles, **so that** I can understand the content at a glance without reading the full text.
   - **Tasks:** 
     - Add the AI assisted search to the python file
     - Create a method to call the newly added python functionality in index.js
     - Create a javascript page in the frontend to allow the user to access the functionality and see the results.

## Team Capacity
- Total hours available: 150 hours (combined team).
- Estimated workload: 130 hours.

## Tasks Breakdown
| Task                      | Assignee      | Estimated Time | Dependencies         |
|---------------------------|---------------|----------------|----------------------|
| Research and select crawling libraries    | Jordi Nakahara  | 3 hours       | None                 |
| Write a script to crawl based on a URL | Harman Goraya   | 10 hours       | Task 1        |
| Store crawled data in a structured format  | Kashif Syed   | 10 hours       | Task 2     |
| Research AI-powerered predictions| Harman Goraya   | 3 hours       | None    |
| Create the functionality in python | Kashif Syed   | 20 hours       | Task 4                 |
| Use index.js to communicate the results of the prediction to the frontend | Maaz Siddiqui   | 20 hours       |   Task 5               |
| Add the AI assisted search to the python file |  Maaz Siddiqui  | 15 hours       | None                 |
| Create a method to call the newly added python functionality in index.js | Maaz Siddiqui   | 15 hours       | Task 7                 |
| Create a javascript page in the frontend to allow the user to access the functionality and see the results | Jordi Nakahara   | 25 hours       | Task 8                 |

## Decisions
 - Use axios to communicate to the back end
 - Utilize AI to quickly summarize a given URL
 - Use BeautifulSoup for crawling

## Risks and Mitigations
- **Risk:** Crawling blocked by some servers.
  - **Mitigation:** Use appropriate headers and rate-limiting.
- **Risk:** Team underestimates task complexities.
  - **Mitigation:** Allocate buffer time for key tasks.

## Deliverables
1. Fully functional AI-based summary tool
2. Fully functional crawling tool