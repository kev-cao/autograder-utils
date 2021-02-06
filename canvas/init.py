import json

if __name__ == '__main__':
    config = {}

    print('Canvas API Initialization\n-------------------------')
    print('You will need the following information:')
    print('1. Canvas API Key')
    print("\tYou must request an API key from your university.")
    print('2. Canvas API URL')
    print("\tYou should be able to find this from your university's tech staff.")
    print('3. Canvas Course ID')
    print("\tYou can find this in the URL of your course's main webpage on Canvas: *.instructure.com/courses/:course_id_here\n\n")

    config['canvas_key'] = input('Please provide your Canvas API key:\n')

    url = input('Please provide the Canvas API URL (must start with https):\n')
    if (url[-1] != '/'):
        url += '/'
    config['canvas_url'] = url

    config['course_id'] = input('Please provide the Canvas Course ID:\n')

    with open('./utils/config.json', 'w') as f:
        json.dump(config, f, indent=4)
