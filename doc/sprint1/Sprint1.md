# Sprint 1 Planning Document (sprint1.md)

**Date:** November 7, 2024  
**Sprint Duration:** November 7 – November 20, 2024  

## Participants
- Jordi Nakahara (Product Owner)
- Harman Goraya (Back End Developer)
- Kashif Syed (Back End Developer)
- Maaz Siddiqui (Front End Developer)

## Sprint Goal
Build a basic data collection and indexing system for CNN’s data to support search functionality.

## User Stories for Sprint 1
1. **Story 1:** Set up the crawling infrastructure.
   - **Tasks:** 
     - Research and select crawling libraries.
     - Write a script to crawl CNN articles.
     - Store crawled data in a structured format.
2. **Story 2:** Design and implement the indexing mechanism.
   - **Tasks:** 
     - Select an indexing structure (e.g., inverted index).
     - Implement indexing algorithm.
     - Test indexing efficiency.
3. **Story 3:** Design and implement the front end and connection of front end and back end.
   - **Tasks:** 
     - Create HTML files for front end.
     - Use JS and/or JSON for connections.
     - Test front end and connection.

## Team Capacity
- Total hours available: 120 hours (combined team).
- Estimated workload: 100 hours.

## Tasks Breakdown
| Task                      | Assignee      | Estimated Time | Dependencies         |
|---------------------------|---------------|----------------|----------------------|
| Set up crawling script    | Developer A   | 20 hours       | None                 |
| Design indexing structure | Developer A   | 15 hours       | Crawled data         |
| Implement indexing logic  | Developer A   | 25 hours       | Design completed     |
| Connect front and back end| Developer B   | 10 hours       | Ends are finished    |
| Design Front End          | Developer B   | 10 hours       | None                 |

## Decisions
- Use `BeautifulSoup` and `requests` for crawling.
- Store data in JSON format for simplicity.
- Opt for an inverted index as the indexing structure.

## Risks and Mitigations
- **Risk:** Crawling blocked by CNN servers.
  - **Mitigation:** Use appropriate headers and rate-limiting.
- **Risk:** Team underestimates task complexities.
  - **Mitigation:** Allocate buffer time for key tasks.

## Deliverables
1. Fully functional crawler for CNN articles.
2. A tested indexing mechanism.
3. Documentation on crawling and indexing processes.
