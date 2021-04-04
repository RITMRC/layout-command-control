# Architecture

## Code Layout

Two primary applications reside in this codebase.
The **brain** and the **leaf**

### Brain

- Interact with the NCE Power Pro Command Station using its RS232 Serial Interface.
- Provide updates to Leaf and take commands from Leaf

### Leaf

- Interface with physical control panels and provide status and read input