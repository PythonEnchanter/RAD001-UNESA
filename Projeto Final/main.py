import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
window_height = 600
window_width = 1000

window_xcoord = (root.winfo_screenwidth() // 2) - (window_width // 2)
window_ycoord = (root.winfo_screenheight() // 2) - (window_height // 2)

def onButtonClick():
    label.config(text="Button Clicked!")

'''def keyPress(event):
    label.config(text=f"{event.char} pressed\n")
'''

root.geometry(f"{window_width}x{window_height}+{window_xcoord}+{window_ycoord}")
root.title("Basic Window")
'''root.bind("<KeyPress>", keyPress)'''

#x--------------BOOK SELECTOR SECTION--------------X
# Create a frame to hold the canvas and the scrollbars
bookslct_frame1 = tk.Frame(root, width=600, height=450)
bookslct_frame1.grid(column=0, row=0)

# Create a Canvas widget
cv_book_selection = tk.Canvas(bookslct_frame1, bg="white")
cv_book_selection.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add vertical scrollbar
v_scrollbar = tk.Scrollbar(bookslct_frame1, orient=tk.VERTICAL, command=cv_book_selection.yview, width=20)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure canvas to use the vertical scrollbar
cv_book_selection.configure(yscrollcommand=v_scrollbar.set)

# Create an inner frame to hold widgets inside the canvas
bookslct_frame2 = tk.Frame(cv_book_selection)

# Add the inner frame to the canvas
cv_book_selection.create_window((0, 0), window=bookslct_frame2, anchor="nw")

# Populate the inner frame with some widgets (e.g., Labels)
for i in range(5):
    for j in range(10):
        tk.Button(bookslct_frame2, text=f"Label {(i+1)*(j+1)}").grid(column=i, row=j)

# Update the scrollable region after adding widgets
bookslct_frame2.update_idletasks()
cv_book_selection.config(scrollregion=cv_book_selection.bbox("all"))
#x--------------BOOK SELECTOR SECTION--------------X

#x--------------USER INFORMATION SECTION-----------X
# Create a frame to hold the canvas and the scrollbars
user_frame1 = tk.Frame(root, width=200, height=450)
user_frame1.grid(column=1, row=0)

# Create a Canvas widget
cv_user_info = tk.Canvas(user_frame1, bg="white")
cv_user_info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add vertical scrollbar
v_scrollbar = tk.Scrollbar(user_frame1, orient=tk.VERTICAL, command=cv_user_info.yview, width=20)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure canvas to use the vertical scrollbar
cv_user_info.configure(yscrollcommand=v_scrollbar.set)

# Create an inner frame to hold widgets inside the canvas
user_frame2 = tk.Frame(cv_user_info)

# Add the inner frame to the canvas
cv_user_info.create_window((0, 0), window=user_frame2, anchor="nw")

# Populate the inner frame with some widgets (e.g., Labels)
'''for i in range(5):
    for j in range(10):
        tk.Button(inner_frame, text=f"Label {(i+1)*(j+1)}").grid(column=i, row=j)
'''
# Update the scrollable region after adding widgets
user_frame2.update_idletasks()
cv_user_info.config(scrollregion=cv_user_info.bbox("all"))
#x--------------USER INFORMATION SECTION-----------X

#x--------------BOOK INFORMATION SECTION-----------X
# Create a frame to hold the canvas and the scrollbars
bookinf_frame1 = tk.Frame(root, width=600, height=150)
bookinf_frame1.grid(column=0, row=1)

tk.Label(bookinf_frame1, text=f"Label __BOOK NAME__").pack()
#x--------------BOOK INFORMATION SECTION-----------X

#x--------------BUTTON/USAGE SECTION---------------X
# Create a frame to hold the canvas and the scrollbars
btt_frame1 = tk.Frame(root, width=200, height=150)
btt_frame1.grid(column=1, row=10)

# Populate the inner frame with some widgets (e.g., Labels)
for i in range(3):
    for j in range(3):
        tk.Button(btt_frame1, text=f"Label {(i+1)*(j+1)}").grid(column=i, row=j)

#x--------------BUTTON/USAGE SECTION---------------X

root.mainloop()
