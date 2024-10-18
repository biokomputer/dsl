# TODO

+ unit tests
+ move sourcecode to python https://github.com/biokomputer/python


 python main.py 
Traceback (most recent call last):
  File "/home/tom/github/biokomputer/dsl/main.py", line 38, in <module>
    main()
  File "/home/tom/github/biokomputer/dsl/main.py", line 30, in main
    run_fungi_simulation(simulation)
  File "/home/tom/github/biokomputer/dsl/src/biocomp/fungi.py", line 31, in run_simulation
    N = simulation.initial_population
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Simulation' object has no attribute 'initial_population'