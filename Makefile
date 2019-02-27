clean: models
	rm -rf models

models:
	pipenv run python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose