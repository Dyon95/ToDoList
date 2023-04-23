# ToDoList

For this To Do List API I want to be able to see all the items, all the to do items, the completed items and the deleted items. 
I also want to be able to add items and update the items, both description and status. 
It is my first project with Python and FastAPI using an SQLite db. 

Thought process:
As I want to have 4 lists of All, To Do, Done & Deleted I need to have 4 different get methods that uses the status as filter. 

Next I want to have 2 update methods, one for the description and one for the status, the status should only be populated with the values of 'To Do', 'Done' & 'Deleted'. 

Because we want to have a list of the deleted items it is not an actual delete from the database, however I will add one more method to completely remove an item but this item will then not show anymore in the deleted list.  