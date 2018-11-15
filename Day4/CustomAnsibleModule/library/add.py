#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def add(firstInput, secondInput):
   return firstInput + secondInput 

def main():
    module = AnsibleModule(
        argument_spec=dict(
            firstInput=dict(type='float', required='yes'),
            secondInput=dict(type='float', required='yes')
        )
    )

    number1 = module.params['firstInput']
    number2 = module.params['secondInput']
    result = add( number1, number2 )
    module.exit_json(meta=result, changed=False)
    #module.fail_json(msg="*******Fatal error occured*******")

main()
