![Tkinter Conway](https://user-images.githubusercontent.com/8599598/73620303-3f591080-45ff-11ea-91c3-cb04c4dcfcdd.JPG)
# Conway's Game of Life using Tkinter
This is a poorly implemented version of Conway's Game of Life.
Cells act very strangely when aproaching edges creating what I call
"edge cascades". Cases where growth rate becomes exponential on edges.
The GUI classes should 100% be seperated from the logical functions.
Due to Tkinter's performance, it will not be updated. Using pyGame
to reimplement this more correctly with better performance.
