version:
	figlet -ckt  "nexo v0.5"
clean:
	figlet -ckt  cleaning
	python3.6 clean.py
	cowsay all done
build:
	figlet -ckt  building
	python3.6 run_build.py
train:
	figlet -ckt  training
	python3.6 run_train.py
list:
	argo list
edit:
	vim sample-args.txt
bconf:
	vim run_build.py
tconf:
	vim run_train.py
models:
	kubectl get sdep
