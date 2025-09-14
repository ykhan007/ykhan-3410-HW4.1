# Southwest Airlines Route Finder – Homework 4.1

This project is for Homework 4.1 from the Graph Data Structures lesson. It models part of the Southwest Airlines network as a graph and finds the shortest flight paths between cities.

I used nine cities as the vertices of the graph, including Dallas (DAL) and Louisville (SDF). Each edge in the graph represents a direct Southwest flight between two airports. The program uses Breadth-First Search (BFS) to find the shortest routes in terms of the fewest stops.

---

## How the Program Works
- The graph is created using a dictionary where each airport code points to its connected airports.  
- BFS is used to search the graph and find the shortest path between two airports. BFS is the best choice because all flights are treated as equal distance, so it always gives the path with the fewest stops.  
- The program runs automatically and prints the shortest paths for three trips without asking the user for input:  
  1. Omaha (OMA) → Louisville (SDF)  
  2. Baltimore-Washington (BWI) → Salt Lake City (SLC), and Salt Lake City (SLC) → Portland, ME (PWM)  
  3. Belize City (BZE) → Portland, ME (PWM)

