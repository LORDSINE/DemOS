import tkinter as tk
from tkinter import ttk
import cpu_scheduling
import memory_management
import disk_scheduling
import process_manager
import file_management


class OSSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operating System Algorithm Simulator")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")
        
        # Center the window on screen
        self.center_window()
        
        # Create main container
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Show home screen
        self.show_home()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_home(self):
        self.clear_frame()
        
        # Title
        title_label = tk.Label(
            self.main_frame,
            text="Operating System Algorithm Simulator",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.main_frame,
            text="Select a module to visualize OS algorithms",
            font=("Arial", 14),
            bg="#f0f0f0",
            fg="#7f8c8d"
        )
        subtitle_label.pack(pady=10)
        
        # Create container for scrollable area
        container = tk.Frame(self.main_frame, bg="#f0f0f0")
        container.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)
        
        # Canvas for scrolling
        canvas = tk.Canvas(container, bg="#f0f0f0", highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Frame inside canvas
        button_frame = tk.Frame(canvas, bg="#f0f0f0")
        canvas_window = canvas.create_window((0, 0), window=button_frame, anchor=tk.NW)
        
        # Module buttons
        modules = [
            ("Process Manager", "Create processes with live memory allocation", self.show_process_manager),
            ("CPU Scheduling", "Visualize process scheduling algorithms", self.show_cpu_scheduling),
            ("Memory Management", "Demonstrate memory allocation strategies", self.show_memory_management),
            ("Disk Scheduling", "Simulate disk head movement algorithms", self.show_disk_scheduling),
            ("File Allocation", "Visualize file allocation methods on disk", self.show_file_management)
        ]
        
        for i, (title, description, command) in enumerate(modules):
            # Create a frame for each button and description
            module_frame = tk.Frame(button_frame, bg="#ffffff", relief=tk.RAISED, borderwidth=2)
            module_frame.pack(pady=10, padx=20, fill=tk.X)
            
            # Module title button
            btn = tk.Button(
                module_frame,
                text=title,
                font=("Arial", 14, "bold"),
                bg="#3498db",
                fg="white",
                activebackground="#2980b9",
                activeforeground="white",
                command=command,
                height=2,
                cursor="hand2",
                relief=tk.FLAT
            )
            btn.pack(padx=20, pady=(20, 5), fill=tk.X)
            
            # Module description
            desc_label = tk.Label(
                module_frame,
                text=description,
                font=("Arial", 10),
                bg="#ffffff",
                fg="#7f8c8d"
            )
            desc_label.pack(padx=20, pady=(0, 20))
        
        # Configure canvas scrolling
        def configure_scroll_region(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
            # Update canvas window width to match canvas width
            canvas.itemconfig(canvas_window, width=canvas.winfo_width())
        
        button_frame.bind("<Configure>", configure_scroll_region)
        canvas.bind("<Configure>", configure_scroll_region)
        
        # Mouse wheel scrolling
        def _on_mousewheel(event):
            try:
                canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            except:
                pass
        
        def _bind_mousewheel(event):
            canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        def _unbind_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")
        
        canvas.bind("<Enter>", _bind_mousewheel)
        canvas.bind("<Leave>", _unbind_mousewheel)
        
        # Footer
        footer_label = tk.Label(
            self.main_frame,
            text="Educational Tool for Understanding Operating System Concepts",
            font=("Arial", 10, "italic"),
            bg="#f0f0f0",
            fg="#95a5a6"
        )
        footer_label.pack(side=tk.BOTTOM, pady=10)
    
    def show_cpu_scheduling(self):
        self.clear_frame()
        cpu_scheduling.CPUSchedulingModule(self.main_frame, self.show_home)
    
    def show_memory_management(self):
        self.clear_frame()
        memory_management.MemoryManagementModule(self.main_frame, self.show_home)
    
    def show_disk_scheduling(self):
        self.clear_frame()
        disk_scheduling.DiskSchedulingModule(self.main_frame, self.show_home)
    
    def show_process_manager(self):
        self.clear_frame()
        process_manager.ProcessManagerModule(self.main_frame, self.show_home)
    
    def show_file_management(self):
        self.clear_frame()
        file_management.FileManagementModule(self.main_frame, self.show_home)


def main():
    root = tk.Tk()
    app = OSSimulatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
