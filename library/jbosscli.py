import os
from ansible.module_utils.basic import *
doublequote = '''"'''
print doublequote


def main():
        fields = {
        "jhome": {"required": True, "type": "str"},
        "cmd": {"required": False, "type": "str"},
        "file": {"required": False, "type": "raw"},
        "mode": {"required": False, "default": "standalone", "type": "str"},
        "configuration": {"required": False, "default": "default",  "type": "str"},
        }
        module = AnsibleModule(argument_spec=fields)
        cmd1 = module.params['cmd']
        home = module.params['jhome']
        mode = module.params['mode']
        file = module.params['file']
        configuration = module.params['configuration']
        if file != None and os.path.isfile(file) == True:
                printCommand = home + '/bin/jboss-cli.sh ' + '--file=' + str(os.path.abspath(file))
        elif mode =="standalone" and file == None:
                printCommand = embdCmd(home,cmd1, configuration)
        else:
                printCommand = ""
        result = {}
        result['command'] = printCommand

        #(rc, out, err) = module.run_command(printCommand, encoding='utf-8')
        (rc, out, err) = module.run_command(printCommand, encoding='utf-8')
        if rc == 0:
                result['out'] = out
                result['err'] = err
                module.exit_json(changed=True, meta=result)

        else:
                result['out'] = out
                result['err'] = err
                module.fail_json(name='jboss-cli', msg=result)


def embdCmd(home, text, configuration):
        command = '''--commands="embed-server,''' + text + '''"'''
        if configuration == "full":
                command = '''--commands="embed-server --server-config=standalone-full.xml,''' + text + '''"'''

        elif configuration == "ha":
                command = '''--commands="embed-server --server-config=standalone-ha.xml,''' + text + '''"'''

        elif configuration == "full-ha":
                command = '''--commands="embed-server --server-config=standalone-full-ha.xml,''' + text + '''"'''
        else:
                command = '''--commands="embed-server,''' + text + '''"'''

        command =  home + '/bin/jboss-cli.sh ' + command
        return command

if __name__ == '__main__':
    main()
