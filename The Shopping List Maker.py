def add_items_to_list(list, item):
    list.append(item)
    return list

list = [1,2,3]
updated_list = add_items_to_list(list, 4)
print(updated_list)



def remove_items_from_a_list(list, item):
    list.pop(item)
    return list


list = [1,2]
extracted_list = remove_items_from_a_list(list, 1)
print(extracted_list)








def entire_list2():
    items = ['pen', 'notepad', 'pencil']
    
    while True:
        action = input("Enter 'add' to add, 'remove' to remove, or 'quit' to quit: ").lower()
        
        if action == 'add':
            new_item = input("Enter an item to add: ")
            items.append(new_item)
            print(f"Added {new_item}. Current items: {items}")
            if 'laptop' in items:
                print("Awesome! Laptop is in the list.")
        
        elif action == 'remove':
            if items:
                removed_item = items.pop()
                print(f"Removed {removed_item}. Current items: {items}")
            else:
                print("The list is empty. Nothing to remove.")
        
        elif action == 'quit':
            print("Quitting...")
            break
        
        else:
            print("Invalid action. Please enter 'add', 'remove', or 'quit'.")


entire_list2()