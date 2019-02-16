from rasa_nlu.model import Metadata, Interpreter
import json

def pprint(o):
 # small helper to make dict dumps a bit prettier
    print(json.dumps(o, indent=2))

interpreter = Interpreter.load('./models/current/nlu')
pprint(interpreter.parse(u"can you follow http://blah.com"))
pprint(interpreter.parse(u"can you watch http://blah.com"))
pprint(interpreter.parse(u"stop watching https://rasa.com/docs/nlu/faq/"))
pprint(interpreter.parse(u"watch https://gitlab-ee-poc.jenkins.release.in.here.com/poit-deploy-scripts/deployment/commits/staging"))
pprint(interpreter.parse(u"status on https://developer.webex.com/docs/bots"))