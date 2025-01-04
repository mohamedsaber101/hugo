#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def main():
    # Define the module's arguments
    module_args = dict(
        string=dict(type='str', required=True)
    )

    # Initialize the AnsibleModule
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Get the input string
    input_string = module.params['string']

    # Check if the string contains any capital letters
    contains_capital = any(char.isupper() for char in input_string)

    # Prepare the result message
    if contains_capital:
        result_message = f"The string '{input_string}' contains capital letters."
    else:
        result_message = f"The string '{input_string}' does not contain any capital letters."

    # Return the result
    module.exit_json(
        changed=False,
        message=result_message,
        contains_capital=contains_capital
    )


if __name__ == '__main__':
    main()

