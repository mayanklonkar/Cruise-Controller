# Cruise-Controller
## Objective

To develop a cruise control for a car which needs to move at a fixed set-point velocity using a PID controller.

## Model 

![image](https://github.com/mayanklonkar/Cruise-Controller/assets/108993449/b78cfe51-a965-4674-a2f4-16b862ee0c92)

If the inertia of the wheels is neglected, and it is assumed that air drag (which is proportional to the car’s speed at low speeds) is opposing the motion of the car, then the problem is reduced to a simple first-order system.

Thus the motion of the car can be written as, mv' + bv = u where u is the input force provided by the engine to move the car at a certain velocity. Though it
is intuitive to think of an input as something related to the gas pedal, but unfortunately to
represent such a system accurately the dynamics of it becomes really complicated for a task of a
beginner level. So for now we will just assume that our engine can give us a certain amount of
force without actually looking how that force translates to real life situations.

## Results
### Parameters
Mass - 1000 kg

Fixed velocity- 100 kmph

Drag coefficient - 1.2

### Velocity v/s Time Plot

![image](https://github.com/mayanklonkar/Cruise-Controller/assets/108993449/2ea56fea-724a-4c9f-b66c-39011d7c5a97)


## Conclusions
Rise time of system (time taken to reach 90% of target velocity) is 5 sec

Maximum overshoot is less than 2 %






