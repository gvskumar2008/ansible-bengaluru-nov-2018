- name: Demonstrates host patterns
  hosts: all[-1] 
  tasks:
    - ping:
