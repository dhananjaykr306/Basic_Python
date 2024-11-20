"""
    @Author: Dhananjay Kumar
    @Date: 03-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 03-10-2024
    @Title:Python Program to Find the Fewest Notes to be returned for Vending Machine
"""

def find_fewest_notes(change, index=0, notes_count=0, notes_returned=[]):
    """ 
    
    Description :
            This function is used to find the fewest notes
    Parameters :
        change: change to be returned

    Return :
            It returns the fewest number of notes for change

    """

    available_notes = [1000, 500, 100, 50, 10, 5, 2, 1]
    if change == 0:
        return notes_count, notes_returned

   
    if available_notes[index] <= change:
        note = available_notes[index]

        notes_returned.append(note)
        notes_count += 1
        return find_fewest_notes(change - note, index, notes_count, notes_returned)
    else:
        return find_fewest_notes(change, index + 1, notes_count, notes_returned)

def vending_machine():
    change = int(input("Enter the change in Rs to be returned: "))
        
    if change <= 0:
        print("Invalid input! The change should be a positive value.")
        return
        
    min_notes, notes_list = find_fewest_notes(change)
        
    print(f"Minimum number of notes needed: {min_notes}")
    print(f"Notes to be returned: {notes_list}")
    

def main():
    
    vending_machine()


if __name__=="__main__":
    main()