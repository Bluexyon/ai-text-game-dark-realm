# DARK REALM v0.1b

This is a modular fantasy adventure Text game powered by AI (AI model I used Lumimaid-v0.2-8B)

## Installation
To install this Program simply download provided Script files and install the necessary libaries.
#### Libraries and Dependencies
- llama-cpp-python
- For Hardware Acceleration only on Nvidea GPUs
    - Nvidea CUDA Toolkit 12.6 Update 3
- AI model I used and recommend Lumimaid-v0.2-8B (I recommend Q4_K_M-imat) with 8gb VRAM
    https://huggingface.co/Lewdiculous/Lumimaid-v0.2-8B-GGUF-IQ-Imatrix

## Usage

To run the Program through the Script first install the dependencies

Using the CPU
```bash
pip install llama-cpp-python
```
If using Hardware Acceleration with an Nvidea GPU
```bash
CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python
```

You need to have an expansion.context file in the expansions folder

then simply type the following in your Terminal:

```bash
python main.py
```

Once in to get the game rolling try asking where you are.

To Quit the Program type exit, quit or end.

## Possible Errors

The AI can bug and repeat output.

The AI can forget what is going on.

If asking the same prompt the AI might give the exact same response it did previously since it takes it's context as priority.

The AI might forget who is who, but it should keep in mind it's the Game Master.

The AI might also not prompt a Death Flag when the user dies.

The AI might ot might not tell you what your current location is.
