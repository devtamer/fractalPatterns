from turtle import * 

color("red", "blue")
begin_fill()
while True:
    setx(30)
    undo()
    sety(30)
    forward(300)
    left(100)
    if abs(pos()) < 1:
        break
end_fill()
done()