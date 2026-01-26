# Operating System Simulator - Interactive OS Environment

A comprehensive, interactive Operating System simulator that behaves like a real OS! Create files, launch processes, manage memory, and watch everything happen in real-time with visual feedback.

## 🎯 Project Overview

This is not just a visualization tool - it's a **working OS simulation** where you can:
- **Create and manage real files** with actual content
- **Launch processes** and watch memory allocation happen
- **See live disk block allocation** when files are created
- **Monitor system resources** in real-time
- Learn OS concepts through hands-on interaction

Perfect for understanding how a real operating system works under the hood!

## ✨ Core Features

### 🖥️ 1. Process Manager - **NEW!**
**Experience real process management:**
- **Create processes** dynamically with custom names and memory requirements
- **Watch live memory allocation** as processes are created
- **View physical memory map** showing exactly where each process lives in RAM
- **Terminate processes** and see memory being freed in real-time
- System and user process separation
- Process details with memory addresses

**What you'll learn:**
- How processes are allocated memory
- Variable partitioning and memory segmentation
- Internal vs external fragmentation
- Process lifecycle management

### 📁 2. File System - **NEW!**
**Create actual files in the simulated OS:**
- **Create files** with names, sizes, and content
- **Write actual text** into files
- **View file contents** in a file viewer
- **Watch disk block allocation** happen in real-time
- **Delete files** and see blocks being freed
- Visual disk allocation map showing which blocks belong to which files

**What you'll learn:**
- How files are stored on disk
- Block allocation strategies
- Disk fragmentation
- File system operations

### 📊 3. OS Dashboard - **NEW!**
**Real-time system monitoring:**
- Live CPU, memory, and disk usage metrics
- Visual memory usage bar chart
- Disk usage pie chart
- Running processes list
- System status and uptime
- Auto-refreshing dashboard

**What you'll learn:**
- System resource monitoring
- Real-time OS metrics
- System performance visualization

### ⚙️ 4. CPU Scheduling
Implements and visualizes:
- **FCFS** - First Come First Serve
- **SJF** - Shortest Job First
- **Priority** - Priority-based scheduling  
- **Round Robin** - Time quantum scheduling

**Features:**
- Interactive Gantt charts
- Waiting time and turnaround time calculations
- Average metrics
- Step-by-step execution

### 💾 5. Memory Management
Implements and visualizes:
- **First Fit** - First available block
- **Best Fit** - Smallest sufficient block
- **Worst Fit** - Largest available block

**Features:**
- Color-coded memory blocks
- Allocation/deallocation operations
- Fragmentation analysis
- Memory utilization statistics

### 💿 6. Disk Scheduling
Implements and visualizes:
- **FCFS**, **SSTF**
- **SCAN**, **C-SCAN**
- **LOOK**, **C-LOOK**

**Features:**
- Disk head movement graphs
- Seek sequence display
- Total seek time calculation

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually comes with Python)

### Installation

1. Clone or download this repository:
```bash
cd OS_Sim
```

2. Verify Python installation:
```bash
python --version
```

3. Check if Tkinter is available:
```bash
python -c "import tkinter; print('Tkinter is installed')"
```

### Running the Simulator

Simply run the main application:
```bash
python main.py
```

## 📖 How to Use

### 🖥️ Process Manager (Start Here!)

**This is like your OS Task Manager on steroids!**

1. **Create Your First Process**:
   - Enter a process name (e.g., "chrome", "calculator")
   - Set memory size (e.g., 32 KB)
   - Click "Create Process"
   - Watch the physical memory map update in real-time!

2. **Quick Create Options**:
   - Click "Small (16KB)" for lightweight processes
   - Click "Medium (32KB)" for normal applications
   - Click "Large (64KB)" for heavy applications

3. **Observe Memory Allocation**:
   - See the memory bar fill up
   - Watch the physical memory map showing exactly where your process lives
   - View memory addresses in hex (like 0x0040, 0x0100)

4. **Process Management**:
   - Select a process → Click "View Details" for full info
   - Click "Terminate Process" to kill it and free memory
   - Watch memory segments merge when processes are killed!

**What's Cool:**
- System processes (kernel, init) are always running
- User processes get dynamic memory allocation
- Memory addresses are shown in hexadecimal (just like real OS!)
- Color coding: Gray=System, Blue=User, White=Free

### 📁 File System (Like Windows Explorer)

**Create actual files with content!**

1. **Create a File**:
   - Enter file name (e.g., "document.txt", "data.json")
   - Set file size (each KB needs 1 disk block)
   - Type actual content in the text area
   - Click "Create File"
   - Watch disk blocks get allocated!

2. **View Files**:
   - Double-click any file in the list
   - See file properties (size, creation time, disk blocks)
   - Read the actual content you typed

3. **Delete Files**:
   - Select file → Click "Delete File"
   - Watch disk blocks become free again
   - See fragmentation reduce

4. **Disk Visualization**:
   - Grid shows all 100 disk blocks (0-99)
   - Each block = 1 KB
   - Colors show which file owns which blocks
   - Free blocks are gray

**Try This:**
- Create 3 small files (5KB each)
- Delete the middle one
- Create a new 8KB file - see how blocks are allocated!

### 📊 OS Dashboard (System Monitor)

**Watch your simulated OS in real-time!**

- Auto-updates every 2 seconds
- CPU usage fluctuates (simulated activity)
- Memory bar shows allocation
- Disk pie chart shows space usage
- Process list shows all running processes
- System uptime counter

**Perfect for demos:** Leave this running during your presentation!

### ⚙️ CPU Scheduling

1. **Select Algorithm**: Choose from FCFS, SJF, Priority, or Round Robin
2. **Add Processes**: 
   - Enter Process ID (e.g., P1)
   - Set Arrival Time
   - Set Burst Time
   - Set Priority (for Priority algorithm)
   - Click "Add Process"
3. **Configure Time Quantum** (for Round Robin only)
4. **Simulate**: Click "Simulate" to run the algorithm
5. **View Results**: See Gantt chart and calculated metrics

**Example Input:**
```
Process P1: Arrival=0, Burst=5, Priority=2
Process P2: Arrival=1, Burst=3, Priority=1
Process P3: Arrival=2, Burst=8, Priority=3
```

### Memory Management

1. **Select Algorithm**: Choose First Fit, Best Fit, or Worst Fit
2. **Add Memory Blocks**:
   - Enter block size in KB
   - Click "Add Block"
   - Or use "Quick Setup" for preset blocks
3. **Allocate Memory**:
   - Enter Process ID
   - Enter size needed
   - Click "Allocate Memory"
4. **Deallocate**: Enter Process ID and click "Deallocate Process"
5. **View Statistics**: See memory utilization and fragmentation

**Quick Setup Creates:**
- Block B1: 100 KB
- Block B2: 200 KB
- Block B3: 300 KB
- Block B4: 150 KB
- Block B5: 250 KB

### Disk Scheduling

1. **Select Algorithm**: Choose from 6 disk scheduling algorithms
2. **Configure Parameters**:
   - Set Initial Head Position (e.g., 50)
   - Set Disk Size (e.g., 200 tracks)
   - Set Direction for SCAN/LOOK algorithms
3. **Add Requests**:
   - Enter track numbers
   - Click "Add Request"
   - Or use "Quick Setup" for example requests
4. **Simulate**: Click "Simulate" to run the algorithm
5. **View Results**: See head movement graph and seek time

**Example Requests:** 98, 183, 37, 122, 14, 124, 65, 67

## 🏗️ Project Structure

```
OS_Sim/
│
├── main.py                    # Main application entry point
├── process_manager.py         # NEW: Process & memory management
├── cpu_scheduling.py          # CPU scheduling algorithms & GUI
├── memory_management.py       # Memory allocation algorithms & GUI
├── disk_scheduling.py         # Disk scheduling algorithms & GUI
├── utils.py                   # Utility functions and helpers
├── test_simulator.py          # Test suite
├── QUICKSTART.py              # Interactive quick start guide
└── README.md                  # This file
```

## 🎓 Educational Value - Now Even Better!

### What Makes This Special:

1. **It's Interactive** - You don't just watch, you DO
2. **Real-time Feedback** - See immediate results of your actions
3. **Live Allocation** - Watch memory/disk allocation happen
4. **Actual Content** - Files have real content, not just metadata
5. **System Simulation** - Behaves like a mini operating system

### For Students:
- ✅ Create files and see disk allocation (not just theory!)
- ✅ Launch processes and watch memory management
- ✅ Understand fragmentation through interaction
- ✅ Learn by doing, not just reading
- ✅ Perfect for viva demonstrations

### For Educators:
- ✅ Live demonstrations in class
- ✅ Students can experiment themselves
- ✅ Shows cause-and-effect clearly
- ✅ Bridges theory and practice
- ✅ Memorable learning experiences

### Key Learning Outcomes:
1. **Process Management**: How OS allocates memory to processes
2. **File Systems**: How files map to disk blocks
3. **Memory Allocation**: Variable partitioning and fragmentation
4. **Resource Management**: System vs user resources
5. **Real-time Monitoring**: How OS tracks resource usage
6. **Algorithm Comparison**: Different strategies, different results

### CPU Scheduling

**FCFS (First Come First Serve)**
- Complexity: O(n)
- Non-preemptive
- May suffer from convoy effect

**SJF (Shortest Job First)**
- Complexity: O(n²) or O(n log n) with priority queue
- Non-preemptive
- Minimizes average waiting time
- May cause starvation

**Priority Scheduling**
- Complexity: O(n²) or O(n log n) with priority queue
- Non-preemptive
- Lower number = Higher priority
- May cause starvation

**Round Robin**
- Complexity: O(n)
- Preemptive with time quantum
- Fair to all processes
- Context switching overhead

### Memory Management

**First Fit**
- Complexity: O(n)
- Fast allocation
- May cause fragmentation

**Best Fit**
- Complexity: O(n)
- Minimizes wasted space
- Slower than First Fit

**Worst Fit**
- Complexity: O(n)
- Leaves largest fragments
- May increase overall fragmentation

### Disk Scheduling

**FCFS**
- Serves requests in arrival order
- Fair but inefficient

**SSTF**
- Chooses closest request
- May cause starvation

**SCAN**
- Elevator algorithm
- Moves to disk end then reverses

**C-SCAN**
- Circular SCAN
- More uniform wait times

**LOOK**
- Like SCAN but reverses at last request

**C-LOOK**
- Circular LOOK
- Most efficient in practice

## 🎓 Educational Value

### For Students:
- Visual understanding of abstract concepts
- Step-by-step algorithm execution
- Comparison of different algorithms
- Hands-on experimentation

### For Educators:
- Classroom demonstration tool
- Viva/demo preparation
- Algorithm comparison teaching
- Interactive learning platform

### Key Learning Outcomes:
1. Understanding process scheduling tradeoffs
2. Memory allocation strategies
3. Disk I/O optimization
4. Performance metrics calculation
5. Algorithm complexity analysis

## 💡 Tips for Viva/Demo

### Preparation Points:

1. **Understand the Logic**: Each algorithm is implemented with clear comments
2. **Know the Metrics**: 
   - Waiting Time = Turnaround Time - Burst Time
   - Turnaround Time = Completion Time - Arrival Time
   - Seek Time = Sum of head movements
3. **Explain Tradeoffs**: Discuss advantages and disadvantages
4. **Use Examples**: Quick setup provides good demo data
5. **Show Comparisons**: Run same input on different algorithms

### Common Demo Questions:

**CPU Scheduling:**
- What is convoy effect in FCFS?
- Why might SJF cause starvation?
- When is Round Robin preferred?

**Memory Management:**
- What is internal vs external fragmentation?
- Which fit algorithm minimizes wasted space?
- How to reduce fragmentation?

**Disk Scheduling:**
- Why is FCFS inefficient for disks?
- What's the difference between SCAN and LOOK?
- When is C-SCAN better than SCAN?

## 🛠️ Technical Details

### Technologies Used:
- **Language**: Python 3.7+
- **GUI Framework**: Tkinter
- **Standard Libraries**: time, math, collections

### Design Principles:
- **Modular Architecture**: Each module is independent
- **Clean Code**: Well-commented and readable
- **Educational Focus**: Clarity over complexity
- **Extensible**: Easy to add new algorithms

### Code Structure:
- **Separation of Concerns**: GUI and logic separated
- **Object-Oriented**: Classes for processes, blocks, etc.
- **Deterministic**: Same input produces same output
- **Commented**: Every algorithm has explanation

## 🔧 Customization

### Adding a New CPU Scheduling Algorithm:

1. Add algorithm function in `cpu_scheduling.py`
2. Follow the pattern of existing algorithms
3. Update the radio button list
4. Add algorithm info to `utils.py`

Example:
```python
def simulate_custom_algorithm(self):
    """Your algorithm implementation"""
    # Calculate schedule
    # Populate self.gantt_data
    # Calculate metrics
    pass
```

### Modifying Visualizations:

All drawing code is in module-specific files:
- Gantt charts: `cpu_scheduling.py` → `draw_gantt_chart()`
- Memory blocks: `memory_management.py` → `draw_memory_visualization()`
- Disk movement: `disk_scheduling.py` → `draw_visualization()`

## 📝 Known Limitations

1. **No Animation Speed Control**: Visualizations are instant
2. **Limited to 20 Processes**: For readability in CPU scheduling
3. **Static Disk Size**: Cannot change during simulation
4. **No Save/Load**: Cannot save configurations

## 🐛 Troubleshooting

### Tkinter Not Found:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS (with Homebrew)
brew install python-tk

# Windows
# Reinstall Python with Tkinter option checked
```

### Window Too Small:
- Maximize the window manually
- Check screen resolution (minimum 1024x768 recommended)

### Algorithms Not Working:
- Ensure all input fields have valid numbers
- Check that processes/blocks/requests are added
- Verify parameters are within valid ranges

## 🤝 Contributing

This is an educational project. Feel free to:
- Add new algorithms
- Improve visualizations
- Fix bugs
- Enhance documentation

## 📄 License

This project is created for educational purposes. Feel free to use, modify, and distribute for learning.

## 👨‍💻 Author

Created for Operating Systems course (SEM-5)
CS23 Batch

## 🙏 Acknowledgments

- OS course curriculum and concepts
- Classic OS algorithm implementations
- Tkinter documentation and examples

## 📚 References

1. Operating System Concepts (Silberschatz, Galvin, Gagne)
2. Modern Operating Systems (Andrew S. Tanenbaum)
3. Operating Systems: Three Easy Pieces (Remzi H. Arpaci-Dusseau)

---

**Happy Learning! 🎓**

For questions or issues, refer to the code comments or OS textbooks for algorithm details.
