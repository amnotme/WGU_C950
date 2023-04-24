### Dijkstra's shortest path example.

The following program sets up a Graph object to represent the above graph, and then runs Dijkstra's shortest path algorithm to find the shortest path from vertex A to all other vertices.

Try changing the weights of some of the edges to see the result in the shortest paths. In each case, can you anticipate which shortest paths will change?




```txt
A to A: A (total weight: 0)
A to B: A -> B (total weight: 8)
A to C: A -> D -> C (total weight: 4)
A to D: A -> D (total weight: 3)
A to E: A -> D -> C -> E (total weight: 6)
A to F: A -> D -> C -> E -> F (total weight: 10)
A to G: A -> D -> C -> E -> F -> G (total weight: 11)
```

- change (A, C) from 7 to 2

```txt
A to A: A (total weight: 0)
A to B: A -> B (total weight: 8)
A to C: A -> C (total weight: 2)
A to D: A -> D (total weight: 3)
A to E: A -> C -> E (total weight: 4)
A to F: A -> C -> E -> F (total weight: 8)
A to G: A -> C -> E -> F -> G (total weight: 9)

```
- change (F, G) from 1 to 10

```txt
A to A: A (total weight: 0)
A to B: A -> B (total weight: 8)
A to C: A -> D -> C (total weight: 4)
A to D: A -> D (total weight: 3)
A to E: A -> D -> C -> E (total weight: 6)
A to F: A -> D -> C -> E -> F (total weight: 10)
A to G: A -> D -> G (total weight: 15)
```
- change (B, E) from 6 to 20

```txt
A to A: A (total weight: 0)
A to B: A -> B (total weight: 8)
A to C: A -> D -> C (total weight: 4)
A to D: A -> D (total weight: 3)
A to E: A -> D -> C -> E (total weight: 6)
A to F: A -> D -> C -> E -> F (total weight: 10)
A to G: A -> D -> C -> E -> F -> G (total weight: 11)
```
