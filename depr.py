from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--name", dest="name", help="Il tuo nome")
parser.add_option("-a", "--age", dest="age", type="int", help="La tua età")

(options, args) = parser.parse_args()

if options.name and options.age:
    print(f"Ciao {options.name}, hai {options.age} anni.")
else:
    print("Per favore specifica nome ed età con -n e -a.")
