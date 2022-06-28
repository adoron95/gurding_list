"# gurding_list" 
An application designed for a security company designed to prevent tampering with the placement of guards.
The application receives constraints and requirements for a database and according to an algorithm saves a slot for the desired month.
In a represented project a guard is saved by requests per month, dates on which he can save and dates on which he cannot save, requests are represented by a list. In addition, each guard has the number of times he has saved so that we can maintain an annual justice table so that the guards are balanced.
Each guard has a phone number stored in the system so that we can attach a text message reminder to the guard in the future.

All guards are represented in a HASH TABLE in this Python implemented by a dictionary.
The application in HASH TABLE gives their organization efficiency while running and memory.

After representing all the guards, we represented them in non-volatile memory as a JSON file.

To arrange the actual conversions I built a parent department and inheritance departments one for the middle of the week and one for the weekend.
The algorithm sorts the constraint lists from the largest to the smallest and begins with an inlay for those who have the most constraints and will consider everyone's desires.

In DEADLOCK mode there is a random selection of a guard.

The entire application has a user-friendly interface that allows you to add a delete deletion and save the list requests in the calendar platform as a PNJ file.
