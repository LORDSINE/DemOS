# DemOS - Technical Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture & Design](#architecture--design)
3. [Technology Stack](#technology-stack)
4. [Core Modules](#core-modules)
5. [Algorithm Implementations](#algorithm-implementations)
6. [Data Structures](#data-structures)
7. [UI/UX Components](#uiux-components)
8. [Performance Analysis](#performance-analysis)
9. [Code Structure](#code-structure)

---

## Project Overview

### Project Name
**DemOS** - Demonstration Operating System Simulator

### Purpose
An educational desktop application designed to visualize and demonstrate core operating system concepts including CPU scheduling algorithms, memory management strategies, disk scheduling algorithms, and process management with live memory allocation.

### Target Audience
- Computer Science students learning Operating Systems
- Educators teaching OS concepts
- Anyone interested in understanding OS algorithms visually

### Key Features
- **Interactive Visualizations**: Real-time graphical representation of algorithms
- **Multiple Algorithms**: 13+ different OS algorithms across 4 modules
- **Live Metrics**: Calculation and display of performance metrics
- **User-Friendly**: Intuitive GUI with easy data input
- **Educational Focus**: Clear explanations and step-by-step execution

---

## Architecture & Design

### System Architecture

```
┌─────────────────────────────────────────────────────┐
│                    main.py (Entry Point)            │
│              OSSimulatorApp (Main Controller)       │
└─────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
┌───────▼───────────┐            ┌──────────▼──────────┐
│   Module Layer    │            │   Utility Layer     │
│  - cpu_scheduling │            │     utils.py        │
│  - memory_mgmt    │            │  - Color utils      │
│  - disk_sched     │            │  - Drawing utils    │
│  - process_mgr    │            │  - Validators       │
└───────────────────┘            │  - Algorithm info   │
                                 └─────────────────────┘
```

### Design Principles

1. **Modular Architecture**: Each OS concept is encapsulated in its own module
2. **Separation of Concerns**: UI logic separated from algorithm logic
3. **Object-Oriented Design**: Processes, blocks, and requests as objects
4. **Single Responsibility**: Each class/function has one clear purpose
5. **DRY Principle**: Common utilities extracted to utils.py
6. **Educational Clarity**: Code readability prioritized over optimization

### Design Patterns Used

- **Module Pattern**: Each scheduling/management system is a self-contained module
- **Callback Pattern**: Back navigation using callback functions
- **Factory Pattern**: Dynamic creation of UI components
- **Observer Pattern**: Real-time updates to visualizations

---

## Technology Stack

### Programming Language
- **Python 3.8+**
  - Chosen for ease of learning and rapid development
  - Cross-platform compatibility
  - Rich standard library

### GUI Framework
- **Tkinter (tk)**
  - Built-in with Python (no external dependencies)
  - Lightweight and fast
  - Sufficient for educational purposes
  - Cross-platform (Windows, macOS, Linux)

### Standard Libraries Used

| Library | Purpose | Usage |
|---------|---------|-------|
| `tkinter` | GUI framework | All UI components |
| `ttk` | Themed widgets | Tables (Treeview), styled UI |
| `time` | Time operations | Timestamps, delays |
| `random` | Random generation | Process priorities |
| `typing` | Type hints | Code documentation |
| `collections` | Data structures | Queues, deques |
| `math` | Mathematical operations | Calculations |

### No External Dependencies
The project intentionally uses only Python standard libraries to:
- Simplify installation
- Ensure portability
- Minimize compatibility issues
- Focus on core concepts

---

## Core Modules

### 1. main.py - Application Entry Point

**Purpose**: Main application controller and home screen

**Key Components**:
- `OSSimulatorApp` class: Main application controller
- Window management and centering
- Navigation between modules
- Scrollable home screen with module cards

**Key Functions**:
```python
def __init__(self, root)              # Initialize application
def center_window(self)               # Center window on screen
def clear_frame(self)                 # Clear current view
def show_home(self)                   # Display home screen
def show_cpu_scheduling(self)         # Navigate to CPU module
def show_memory_management(self)      # Navigate to Memory module
def show_disk_scheduling(self)        # Navigate to Disk module
def show_process_manager(self)        # Navigate to Process module
```

**UI Layout**:
- Header: Application title and subtitle
- Body: Scrollable canvas with 4 module cards
- Each card: Title button + description
- Footer: Educational tagline

**Window Specifications**:
- Default size: 1200x800 pixels
- Centered on screen
- Background: #f0f0f0 (light gray)

---

### 2. cpu_scheduling.py - CPU Scheduling Module

**Purpose**: Simulate and visualize CPU scheduling algorithms

#### Algorithms Implemented

##### 2.1 FCFS (First Come First Serve)
**Algorithm**: Non-preemptive, processes execute in arrival order

**Implementation**:
```python
def simulate_fcfs(self):
    # Sort by arrival time
    sorted_processes = sorted(self.processes, key=lambda p: p.arrival_time)
    
    current_time = 0
    for process in sorted_processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        
        process.start_time = current_time
        process.completion_time = current_time + process.burst_time
        current_time = process.completion_time
        
        # Calculate metrics
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
```

**Time Complexity**: O(n log n) - sorting dominates
**Space Complexity**: O(n) - Gantt chart data

**Advantages**:
- Simple to implement
- Fair (FIFO order)
- No starvation

**Disadvantages**:
- Convoy effect (long processes block short ones)
- High average waiting time
- Not suitable for time-sharing systems

##### 2.2 SJF (Shortest Job First)
**Algorithm**: Non-preemptive, shortest burst time executes first

**Implementation**:
```python
def simulate_sjf(self):
    remaining = self.processes.copy()
    current_time = 0
    
    while remaining:
        # Get available processes
        available = [p for p in remaining if p.arrival_time <= current_time]
        
        if not available:
            current_time = min(p.arrival_time for p in remaining)
            continue
        
        # Select shortest job
        process = min(available, key=lambda p: p.burst_time)
        # Execute process...
```

**Time Complexity**: O(n²) - nested selection
**Space Complexity**: O(n)

**Advantages**:
- Minimizes average waiting time
- Optimal for non-preemptive scheduling

**Disadvantages**:
- Starvation of long processes
- Requires burst time prediction
- Not practical in real systems

##### 2.3 Priority Scheduling
**Algorithm**: Processes execute based on priority (lower number = higher priority)

**Implementation**:
```python
def simulate_priority(self):
    remaining = self.processes.copy()
    current_time = 0
    
    while remaining:
        available = [p for p in remaining if p.arrival_time <= current_time]
        
        if not available:
            current_time = min(p.arrival_time for p in remaining)
            continue
        
        # Select highest priority (lowest number)
        process = min(available, key=lambda p: (p.priority, p.arrival_time))
        # Execute...
```

**Time Complexity**: O(n²)
**Space Complexity**: O(n)

**Advantages**:
- Important processes execute first
- Flexible priority assignment

**Disadvantages**:
- Low-priority process starvation
- Priority inversion problems
- Requires priority assignment

##### 2.4 Round Robin (RR)
**Algorithm**: Preemptive, each process gets time quantum in circular order

**Implementation**:
```python
def simulate_rr(self):
    time_quantum = int(self.time_quantum_var.get())
    queue = []
    current_time = 0
    remaining = sorted(self.processes, key=lambda p: p.arrival_time)
    
    while remaining or queue:
        # Add arrived processes to queue
        while remaining and remaining[0].arrival_time <= current_time:
            queue.append(remaining.pop(0))
        
        if not queue:
            current_time = remaining[0].arrival_time
            continue
        
        process = queue.pop(0)
        execution_time = min(time_quantum, process.remaining_time)
        process.remaining_time -= execution_time
        current_time += execution_time
        
        # Re-queue if not finished
        if process.remaining_time > 0:
            queue.append(process)
```

**Time Complexity**: O(n × burst_time / quantum)
**Space Complexity**: O(n) - queue

**Advantages**:
- Fair CPU allocation
- Good for time-sharing systems
- No starvation
- Responsive

**Disadvantages**:
- Context switching overhead
- Performance depends on quantum size
- Higher average turnaround time

#### Performance Metrics

**Calculated for each algorithm**:
1. **Waiting Time**: Time spent in ready queue
   - Formula: Turnaround Time - Burst Time
   
2. **Turnaround Time**: Total time from arrival to completion
   - Formula: Completion Time - Arrival Time
   
3. **Completion Time**: Time when process finishes
   
4. **Response Time**: Time from arrival to first execution
   - Formula: Start Time - Arrival Time

5. **Average Metrics**: Mean of all process metrics

#### Visualization Components
- **Gantt Chart**: Timeline visualization of process execution
- **Process Table**: Input processes with arrival/burst times
- **Results Table**: Completion times and calculated metrics
- **Statistics Panel**: Average waiting/turnaround times

---

### 3. memory_management.py - Memory Allocation Module

**Purpose**: Demonstrate memory allocation strategies

#### Algorithms Implemented

##### 3.1 First Fit
**Algorithm**: Allocate first block large enough

**Implementation**:
```python
def first_fit(self, size):
    for block in self.memory_blocks:
        if not block.is_allocated and block.size >= size:
            return block
    return None
```

**Time Complexity**: O(n) - linear search
**Space Complexity**: O(1)

**Advantages**:
- Fast allocation
- Simple implementation
- Low overhead

**Disadvantages**:
- External fragmentation
- May skip better-fitting blocks

##### 3.2 Best Fit
**Algorithm**: Allocate smallest block that fits

**Implementation**:
```python
def best_fit(self, size):
    suitable_blocks = [b for b in self.memory_blocks 
                       if not b.is_allocated and b.size >= size]
    if not suitable_blocks:
        return None
    return min(suitable_blocks, key=lambda b: b.size)
```

**Time Complexity**: O(n) - full scan required
**Space Complexity**: O(n) - temporary list

**Advantages**:
- Minimizes wasted space
- Better memory utilization

**Disadvantages**:
- Slower than First Fit
- Creates tiny unusable fragments
- More fragmentation overall

##### 3.3 Worst Fit
**Algorithm**: Allocate largest available block

**Implementation**:
```python
def worst_fit(self, size):
    suitable_blocks = [b for b in self.memory_blocks 
                       if not b.is_allocated and b.size >= size]
    if not suitable_blocks:
        return None
    return max(suitable_blocks, key=lambda b: b.size)
```

**Time Complexity**: O(n)
**Space Complexity**: O(n)

**Advantages**:
- Leaves large usable fragments
- Reduces tiny fragment creation

**Disadvantages**:
- Wastes memory
- Large blocks fill quickly
- Poor overall utilization

#### Memory Concepts Demonstrated

1. **Fragmentation**:
   - **Internal**: Wasted space within allocated block
   - **External**: Free space between blocks too small to use

2. **Memory Block States**:
   - Allocated (occupied by process)
   - Free (available for allocation)

3. **Deallocation**: Memory freed when process terminates

#### Visualization
- **Memory Blocks Table**: Shows block size, status, process
- **Allocation History**: Timeline of allocations
- **Visual Memory Map**: Graphical block representation
- **Fragmentation Statistics**: Internal/external fragmentation metrics

---

### 4. disk_scheduling.py - Disk Head Scheduling Module

**Purpose**: Simulate disk head movement algorithms

#### Disk Parameters
- **Track Numbers**: 0 to disk_size (default 0-199)
- **Initial Head Position**: Starting position of read/write head
- **Direction**: For SCAN/LOOK algorithms (left/right)

#### Algorithms Implemented

##### 4.1 FCFS (First Come First Serve)
**Algorithm**: Service requests in order of arrival

**Implementation**:
```python
def fcfs_scheduling(self):
    self.seek_sequence = [self.initial_head] + self.requests
    
    self.total_seek_time = 0
    for i in range(len(self.seek_sequence) - 1):
        self.total_seek_time += abs(self.seek_sequence[i+1] - self.seek_sequence[i])
```

**Seek Time**: Sum of absolute differences between consecutive positions

**Advantages**:
- Fair, no starvation
- Simple implementation

**Disadvantages**:
- High seek time
- No optimization
- Wild head movements

##### 4.2 SSTF (Shortest Seek Time First)
**Algorithm**: Service nearest request first

**Implementation**:
```python
def sstf_scheduling(self):
    current_pos = self.initial_head
    remaining = self.requests.copy()
    self.seek_sequence = [current_pos]
    
    while remaining:
        # Find nearest request
        nearest = min(remaining, key=lambda x: abs(x - current_pos))
        self.seek_sequence.append(nearest)
        self.total_seek_time += abs(nearest - current_pos)
        current_pos = nearest
        remaining.remove(nearest)
```

**Time Complexity**: O(n²) - greedy selection
**Space Complexity**: O(n)

**Advantages**:
- Better than FCFS
- Reduced average seek time
- Good throughput

**Disadvantages**:
- Starvation of distant requests
- Not optimal
- Variance in response time

##### 4.3 SCAN (Elevator Algorithm)
**Algorithm**: Move in one direction, service all requests, then reverse

**Implementation**:
```python
def scan_scheduling(self):
    current_pos = self.initial_head
    direction = self.direction
    
    # Separate requests by direction
    left = sorted([r for r in self.requests if r < current_pos])
    right = sorted([r for r in self.requests if r >= current_pos])
    
    if direction == "left":
        # Go left to 0, then right
        sequence = left[::-1] + [0] + right
    else:
        # Go right to end, then left
        sequence = right + [self.disk_size] + left[::-1]
    
    self.seek_sequence = [current_pos] + sequence
    # Calculate seek time...
```

**Characteristics**:
- Goes to disk boundaries (0 or disk_size)
- Services requests in direction of travel
- Changes direction at boundaries

**Advantages**:
- No starvation
- Predictable
- Good for heavy loads

**Disadvantages**:
- Long wait for opposite direction
- Uneven service time
- Goes to boundary even if no requests

##### 4.4 C-SCAN (Circular SCAN)
**Algorithm**: Move in one direction to end, jump to start, continue

**Implementation**:
```python
def cscan_scheduling(self):
    current_pos = self.initial_head
    
    left = sorted([r for r in self.requests if r < current_pos])
    right = sorted([r for r in self.requests if r >= current_pos])
    
    # Always go right, then wrap to 0 and continue right
    self.seek_sequence = [current_pos] + right + [self.disk_size, 0] + left
```

**Advantages**:
- More uniform wait time
- Better than SCAN for fairness
- Good for heavy loads

**Disadvantages**:
- Higher seek time than SCAN
- Wasteful return jump
- Only services in one direction

##### 4.5 LOOK
**Algorithm**: Like SCAN but doesn't go to boundary, reverses at last request

**Implementation**:
```python
def look_scheduling(self):
    current_pos = self.initial_head
    
    left = sorted([r for r in self.requests if r < current_pos])
    right = sorted([r for r in self.requests if r >= current_pos])
    
    if self.direction == "left":
        sequence = left[::-1] + right
    else:
        sequence = right + left[::-1]
    
    self.seek_sequence = [current_pos] + sequence
```

**Advantages**:
- Better than SCAN
- No wasted movement to boundaries
- Lower seek time

**Disadvantages**:
- Still direction-biased
- Complex implementation

##### 4.6 C-LOOK
**Algorithm**: Like C-SCAN but doesn't go to boundaries

**Implementation**:
```python
def clook_scheduling(self):
    current_pos = self.initial_head
    
    left = sorted([r for r in self.requests if r < current_pos])
    right = sorted([r for r in self.requests if r >= current_pos])
    
    # Go right to last request, jump to first left request, continue right
    self.seek_sequence = [current_pos] + right + left
```

**Advantages**:
- Most uniform wait time
- No boundary movement
- Best overall performance

**Disadvantages**:
- Complex implementation
- Jump overhead still exists

#### Metrics Calculated
1. **Total Seek Time**: Sum of all head movements
2. **Average Seek Time**: Total / number of requests
3. **Seek Sequence**: Order of servicing requests

#### Visualization Features
- **Disk Track Diagram**: Visual representation of disk tracks
- **Head Movement Animation**: Animated disk head movement
- **Seek Sequence Table**: Table showing movement order
- **Graph Visualization**: Line graph showing head movement pattern
- **Pan and Zoom**: Interactive graph navigation

---

### 5. process_manager.py - Process Management Module

**Purpose**: Simulate process creation and dynamic memory allocation

#### Key Features

##### 5.1 Process Management
- Create user and system processes
- Allocate memory dynamically
- Terminate processes
- View process details
- Track process states

##### 5.2 Memory Allocation Strategy
**Algorithm**: First Fit with Variable Partitioning

**Implementation**:
```python
def allocate_memory_to_process(self, name, memory_size, proc_type):
    for i, segment in enumerate(self.memory_segments):
        if not segment.is_allocated and segment.size >= memory_size:
            pid = self.next_pid
            self.next_pid += 1
            
            process = Process(pid, name, memory_size, proc_type)
            
            if segment.size == memory_size:
                # Exact fit
                segment.is_allocated = True
                segment.process_pid = pid
            else:
                # Split segment
                allocated_seg = MemorySegment(segment.start_address, memory_size)
                allocated_seg.is_allocated = True
                allocated_seg.process_pid = pid
                
                free_seg = MemorySegment(
                    segment.start_address + memory_size,
                    segment.size - memory_size
                )
                
                self.memory_segments[i] = allocated_seg
                self.memory_segments.insert(i + 1, free_seg)
            
            self.processes.append(process)
            return True
    
    return False  # Out of memory
```

##### 5.3 Memory Deallocation and Merging
**Algorithm**: Coalescing adjacent free segments

**Implementation**:
```python
def merge_free_segments(self):
    merged = True
    while merged:
        merged = False
        for i in range(len(self.memory_segments) - 1):
            curr = self.memory_segments[i]
            next_seg = self.memory_segments[i + 1]
            
            if not curr.is_allocated and not next_seg.is_allocated:
                # Merge adjacent free segments
                curr.size += next_seg.size
                self.memory_segments.pop(i + 1)
                merged = True
                break
```

**Prevents**: External fragmentation by consolidating free space

#### Data Structures

##### Process Class
```python
class Process:
    pid: int                    # Process ID
    name: str                   # Process name
    memory_size: int            # Memory required (KB)
    process_type: str           # "System" or "User"
    state: str                  # Ready, Running, Waiting, Terminated
    allocated_memory: int       # Start address
    creation_time: str          # HH:MM:SS
    cpu_time: int               # CPU time in ms
    priority: int               # Priority (1-5)
```

##### MemorySegment Class
```python
class MemorySegment:
    start_address: int          # Starting address
    size: int                   # Segment size (KB)
    is_allocated: bool          # Allocation status
    process_pid: int            # Owning process PID
    process_name: str           # Owning process name
```

#### System Configuration
- **Total RAM**: 512 KB
- **Initial Segments**: One 512 KB free block
- **System Processes**: kernel (64 KB), init (16 KB)
- **Addressing**: Hexadecimal (0x0000 to 0x0200)

#### Visualization Components

##### 1. Memory Usage Bar
- Real-time progress bar
- Used memory (red) vs Free memory (green)
- Percentage and KB display

##### 2. Physical Memory Map
- **Scrollable Canvas**: Handles many processes
- **Linear Address Space**: Vertical memory layout
- **Color Coding**:
  - #34495e: System processes (dark blue)
  - #3498db: User processes (blue)
  - #ecf0f1: Free memory (light gray)
- **Minimum Segment Height**: 45px for readability
- **Memory Width**: 300px bars
- **Address Labels**: Hexadecimal on left
- **Process Info**: Name, PID, size displayed

##### 3. Process List Table
- Columns: PID, Name, Memory, State
- Centered alignment for numerical data
- Real-time updates

##### 4. System Statistics
- Process count (system/user)
- Memory utilization percentage
- Segment count and free segments

##### 5. Activity Log
- Scrollable text area
- Timestamped events
- Color: Green text on dark background
- Events: Creation, allocation, termination

#### Mouse Wheel Scrolling
**Implementation**:
```python
def _on_mousewheel(self, event):
    if event.num == 5 or event.delta < 0:
        self.memory_canvas.yview_scroll(1, "units")
    elif event.num == 4 or event.delta > 0:
        self.memory_canvas.yview_scroll(-1, "units")
```

Supports both Windows (delta) and Linux (num) scroll events.

---

### 6. utils.py - Utility Functions

**Purpose**: Shared utilities used across modules

#### Color Utilities

```python
def generate_colors(n: int) -> List[str]
    # Returns n distinct colors for visualization
    # Uses predefined palette, repeats if n > palette size

def lighten_color(color: str, factor: float = 0.3) -> str
    # RGB manipulation to create lighter shade
    
def darken_color(color: str, factor: float = 0.3) -> str
    # RGB manipulation to create darker shade
```

#### Drawing Utilities

```python
def draw_arrow(canvas, x1, y1, x2, y2, color, width)
    # Draw arrow on canvas
    
def draw_grid(canvas, x_start, y_start, width, height, grid_size, color)
    # Draw background grid for graphs
```

#### Statistical Functions

```python
def calculate_average(values: List[float]) -> float
    # Safe average calculation (handles empty list)
    
def format_time(milliseconds: int) -> str
    # Format time: ms → s → m:s
```

#### UI Utilities

```python
def create_tooltip(widget, text)
    # Add hover tooltip to widget
    
def validate_numeric_input(text, allow_negative, allow_decimal) -> bool
    # Validate numeric input fields
    
def center_window(window, width, height)
    # Center window on screen
    
def create_styled_button(parent, text, command, bg_color, ...) -> tk.Button
    # Create consistent styled button
    
def create_info_label(parent, text, bg_color) -> tk.Label
    # Create informational label
```

#### Algorithm Information Database

```python
ALGORITHM_INFO = {
    "FCFS": {
        "name": "First Come First Serve",
        "description": "...",
        "time_complexity": "O(n)",
        "space_complexity": "O(1)"
    },
    # ... all algorithms
}
```

#### Animation Controller Class

```python
class AnimationController:
    def __init__(self)
    def set_steps(self, max_steps)
    def step_forward(self) -> bool
    def step_backward(self) -> bool
    def play(self, root)
    def pause(self)
    def reset(self)
```

**Purpose**: Manages step-by-step algorithm animation

---

## Data Structures

### Process (CPU Scheduling)
- **Attributes**: pid, arrival_time, burst_time, priority, remaining_time
- **Calculated**: completion_time, turnaround_time, waiting_time, start_time
- **Purpose**: Represents a process to be scheduled

### MemoryBlock (Memory Management)
- **Attributes**: block_id, size, is_allocated, process_id
- **Purpose**: Represents a memory partition

### ProcessRequest (Memory Management)
- **Attributes**: process_id, size, allocated_block
- **Purpose**: Represents a memory allocation request

### Process (Process Manager)
- **Attributes**: pid, name, memory_size, process_type, state, allocated_memory
- **Purpose**: Represents a running process with memory

### MemorySegment (Process Manager)
- **Attributes**: start_address, size, is_allocated, process_pid, process_name
- **Purpose**: Represents a contiguous memory segment

### Gantt Chart Data
```python
gantt_data = [(process_id, start_time, duration), ...]
```
- **Purpose**: Timeline visualization data

### Seek Sequence
```python
seek_sequence = [head_position_1, head_position_2, ...]
```
- **Purpose**: Disk head movement sequence

---

## UI/UX Components

### Color Scheme

#### Primary Colors
- **Primary Blue**: #3498db (buttons, user processes)
- **Dark Blue**: #34495e (headers, system processes)
- **Green**: #27ae60 (success, create buttons)
- **Red**: #e74c3c (error, terminate, used memory)
- **Teal**: #16a085 (secondary actions)

#### Background Colors
- **Light Gray**: #ecf0f1 (content background)
- **White**: #ffffff (panels, cards)
- **Dark Gray**: #2c3e50 (text, dark headers)

#### Status Colors
- **Success**: #2ecc71 (green)
- **Warning**: #f39c12 (orange)
- **Error**: #e74c3c (red)
- **Info**: #3498db (blue)

### Typography

- **Title**: Arial, 18pt, Bold
- **Subtitle**: Arial, 14pt, Normal
- **Headers**: Arial, 11-12pt, Bold
- **Body**: Arial, 9-10pt, Normal
- **Monospace**: Courier, 8-9pt (for addresses, logs)

### Layout Structure

#### Standard Module Layout
```
┌──────────────────────────────────────────┐
│ Header (60px, colored background)        │
│ ← Back Button | Module Title             │
├──────────────────────────────────────────┤
│ ┌──────────┬─────────────────────────┐   │
│ │          │                         │   │
│ │  Left    │   Right Panel           │   │
│ │  Panel   │   (Visualization)       │   │
│ │ (Input & │                         │   │
│ │ Control) │                         │   │
│ │          │                         │   │
│ └──────────┴─────────────────────────┘   │
└──────────────────────────────────────────┘
```

- **Left Panel**: Width ~350px, fixed, white background
- **Right Panel**: Expandable, white background
- **Padding**: 10px outer, 5-10px inner

### Interactive Elements

#### Buttons
- **Create/Add**: Green (#27ae60)
- **Remove/Terminate**: Red (#e74c3c)
- **Quick Setup**: Teal (#16a085)
- **Action**: Blue (#3498db)
- **Navigation**: Dark (#2c3e50)

#### Input Fields
- Entry widgets with variable binding
- Default values provided
- Validation on input
- Width: 10-12 characters

#### Tables (Treeview)
- Column headers with text
- Alternating row colors (automatic)
- Scrollable for large data
- Sortable columns

### Responsive Features

1. **Scrollable Canvases**: Handle overflow content
2. **Mouse Wheel Support**: Smooth scrolling
3. **Dynamic Sizing**: Canvas scales with window
4. **Minimum Heights**: Readability on small segments
5. **Tooltips**: Help text on hover
6. **Pan and Zoom**: Interactive graph navigation (disk scheduling)

---

## Performance Analysis

### Algorithmic Complexity

#### CPU Scheduling
| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| FCFS      | O(n log n)     | O(n)            |
| SJF       | O(n²)          | O(n)            |
| Priority  | O(n²)          | O(n)            |
| Round Robin | O(n × T/Q)   | O(n)            |

*where n = number of processes, T = total burst time, Q = quantum*

#### Memory Management
| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| First Fit | O(n)           | O(1)            |
| Best Fit  | O(n)           | O(n)            |
| Worst Fit | O(n)           | O(n)            |

*where n = number of blocks*

#### Disk Scheduling
| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| FCFS      | O(n)           | O(n)            |
| SSTF      | O(n²)          | O(n)            |
| SCAN      | O(n log n)     | O(n)            |
| C-SCAN    | O(n log n)     | O(n)            |
| LOOK      | O(n log n)     | O(n)            |
| C-LOOK    | O(n log n)     | O(n)            |

*where n = number of disk requests*

### GUI Performance

- **Tkinter Rendering**: Fast for educational use
- **Canvas Redraw**: O(n) where n = number of drawn elements
- **Scrolling**: Smooth with reasonable data (< 100 processes)
- **Animation**: 500-1000ms delays for visibility

### Scalability Limits

#### Practical Limits (for good UX):
- **Processes (CPU)**: 20-30 processes
- **Memory Blocks**: 15-20 blocks
- **Disk Requests**: 20-30 requests
- **Process Manager**: 30-40 processes before scrolling

#### Technical Limits:
- Python list/sort operations: Thousands
- Tkinter canvas: Hundreds of items
- Main constraint: Visual clarity, not performance

---

## Code Structure

### File Organization

```
DemOS/
├── main.py                    # Entry point (178 lines)
├── cpu_scheduling.py          # CPU algorithms (568 lines)
├── memory_management.py       # Memory algorithms (540 lines)
├── disk_scheduling.py         # Disk algorithms (676 lines)
├── process_manager.py         # Process management (703 lines)
├── utils.py                   # Utilities (364 lines)
├── README.md                  # User documentation
├── DOCUMENTATION.md           # User manual
├── QUICKSTART.py              # Quick start guide
├── docs/
│   ├── TECHNICAL_DOCUMENTATION.md  # This file
│   └── README.md              # Docs README
└── __pycache__/              # Python bytecode
```

### Code Statistics

- **Total Lines**: ~3,029 lines of Python code
- **Modules**: 6 Python files
- **Classes**: 11 main classes
- **Functions**: 100+ functions/methods
- **Comments**: Extensive docstrings and inline comments

### Coding Standards

1. **PEP 8 Compliance**: Python style guide followed
2. **Docstrings**: All classes and major functions documented
3. **Type Hints**: Used in utils.py for clarity
4. **Naming Conventions**:
   - Classes: PascalCase
   - Functions: snake_case
   - Constants: UPPER_CASE
   - Private: _leading_underscore
5. **Comments**: Explain "why" not "what"
6. **Magic Numbers**: Avoid; use named constants

### Code Quality Features

1. **Error Handling**: Try-except for user input
2. **Input Validation**: Check before processing
3. **Default Values**: Sane defaults for all inputs
4. **User Feedback**: MessageBoxes for errors/confirmations
5. **Edge Cases**: Handle empty lists, zero values
6. **Defensive Programming**: Check before operating

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Tkinter (usually included with Python)

### Installation Steps

1. **Clone/Download** the project
2. **Navigate** to project directory
3. **Run** the application:
   ```bash
   python main.py
   ```

### Verification

Check Python version:
```bash
python --version
```

Check Tkinter availability:
```bash
python -c "import tkinter; print('Tkinter available')"
```

---

## Future Enhancements

### Potential Features

1. **Additional Algorithms**:
   - SRTF (Shortest Remaining Time First)
   - Multilevel Queue Scheduling
   - Paging and Segmentation
   - LRU Page Replacement

2. **Enhanced Visualizations**:
   - 3D graphics
   - Animations with speed control
   - Export visualizations as images

3. **Analysis Tools**:
   - Algorithm comparison mode
   - Export metrics to CSV
   - Statistical analysis

4. **User Experience**:
   - Dark mode theme
   - Customizable colors
   - Save/load scenarios
   - Undo/redo functionality

5. **Educational Features**:
   - Step-by-step explanations
   - Quiz mode
   - Tutorial mode
   - Algorithm complexity graphs

---

## Troubleshooting

### Common Issues

**Issue**: Tkinter not found
**Solution**: Install Python from official source (includes Tkinter)

**Issue**: Window too small/large
**Solution**: Modify geometry in main.py line 13

**Issue**: Canvas not scrolling
**Solution**: Ensure sufficient processes/data created

**Issue**: Animations too fast/slow
**Solution**: Adjust delay in animation controller

---

## References and Resources

### Operating System Concepts
- **Textbook**: Operating System Concepts by Silberschatz, Galvin, Gagne
- **CPU Scheduling**: Chapters on Process Scheduling
- **Memory Management**: Chapters on Memory Allocation
- **Disk Scheduling**: Chapters on Mass Storage

### Python and Tkinter
- **Python Docs**: https://docs.python.org/3/
- **Tkinter Docs**: https://docs.python.org/3/library/tkinter.html
- **Tkinter Tutorial**: https://tkdocs.com/

### Algorithms
- **CLRS**: Introduction to Algorithms by Cormen et al.
- **Wikipedia**: Individual algorithm articles

---

## Contributors and Credits

**Project**: DemOS - Operating System Simulator
**Purpose**: Educational demonstration tool
**Framework**: Python + Tkinter
**License**: Educational use

---

## Version History

- **v1.0**: Initial release with 4 modules
  - CPU Scheduling (4 algorithms)
  - Memory Management (3 algorithms)
  - Disk Scheduling (6 algorithms)
  - Process Manager with dynamic memory

---

## Contact and Support

For questions, issues, or educational use:
- Review the code comments and docstrings
- Check DOCUMENTATION.md for user guide
- Experiment with different inputs

---

*End of Technical Documentation*

**Last Updated**: February 2026
**Document Version**: 1.0
