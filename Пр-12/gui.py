import tkinter as tk
from tkinter import Label, Entry, Button, scrolledtext, messagebox
import requests




def request(url, username):
    get = requests.get(url=url).json()
    if username == 'node':#там японские сиволы в файл не копируются
        filter_get = {
            'company': f'-----',
            'created_at': f'{get['created_at']}',
            'email': f'{get['email']}',
            'id': f'{get['id']}',
            'name': f'-----',
            'url': f'{get['url']}',
        }
    else:
        filter_get = {
            'company': f'{get['company']}',
            'created_at': f'{get['created_at']}',
            'email': f'{get['email']}',
            'id': f'{get['id']}',
            'name': f'{get['name']}',
            'url': f'{get['url']}',
        }
    text.insert(1.0, f'#Info about {username} is saved in a info_about_gituser.txt\n\n{filter_get}')

    with open('info_about_gituser', 'w') as file:
        file.write(f'{username}:\n{filter_get}')




def scrape():
    name = entry.get()
    text.delete('1.0', 'end')
    c = 0 #проходим по блоку try-except и если нет ошибки ввода, то c = 1(счётчик вместо statuscode, т.к. это быстрее)
    try:
        if name in reference_and_name:
            c += 1
            www = reference_and_name.get(name)
        else:
            name = int(name)
            if 1 <= name <= 100:
                c += 1
                www = reference_list[name - 1]
            else:
                raise Exception()
        entry.delete(0, 'end')
        github_url = f"https://api.github.com/users/{www}"
        request(github_url, www)
    except Exception as ex:
        if c == 0:
            error_message = f'Input error\n\nEnter only the number from 1 to 100 or the name of the project as written in the Habr article.'
        else:
            error_message = f'Status 404 or user deleted his page on GitHub'#43 и 94 точно удалили
        entry.delete(0, 'end')
        messagebox.showinfo('Error!!!', error_message, parent=window)




#скопировано из list_txt
reference_and_name = {'Google Kubernetes': 'kubernetes', ' Apache Spark': 'spark', 'Microsoft Visual Studio Code': 'vscode', 'NixOS Package Collection': 'nixpkgs', 'Rust': 'rust', 'Firehol IP Lists': 'blocklist-ipsets', 'Red Hat OpenShift': 'openshift-ansible', 'Ansible': 'ansible', 'Automattic WordPress Calypso': 'wp-calypso', 'Microsoft .NET CoreFX': 'corefx', 'Microsoft .NET Roslyn': 'roslyn', 'Node.js': 'node', 'TensorFlow': 'tensorflow', 'freeCodeCamp': 'freeCodeCamp', 'Space Station 13': 'vgstation13', 'Apple Swift': 'swift', 'Elasticsearch': 'elasticsearch', 'Moby': 'moby', 'CockroachDB': 'cockroach', 'Cydia Compatibility Checker': 'tweakCompatible', 'Servo': 'servo', 'Google Flutter': 'flutter', 'macOS Homebrew Package Manager': 'homebrew-core', 'Home Assistant': 'home-assistant', 'Microsoft .NET CoreCLR': 'coreclr', 'CocoaPods Specifications': 'Specs', 'Elastic Kibana': 'kibana', 'Julia Language': 'julia', 'Microsoft TypeScript': 'TypeScript', 'Joomla': 'joomla-cms', 'DefinitelyTyped': 'DefiniteTyped', 'Homebrew Cask': 'homebrew-cask', 'Ceph': 'ceph', 'Go': 'go', 'AMP HTML Builder': 'amphtml', 'Open edX': 'edx-platform', 'Pandas': 'pandas', 'Istio': 'istio', 'ManageIQ': 'manageiq', 'Godot Engine': 'godot', 'Gentoo Repository Mirror': 'gentoo', 'Odoo': 'odoo', 'Azure Documentation': 'azure-docs', 'Magento': 'magento2', 'Saltstack': 'salt', 'AdGuard Filters': 'AdguardFilters', 'Symfony': 'symfony', 'CMS Software for the Large Hadron Collider': 'cmssw', 'OwnCloud': 'core', 'gRPC': 'grpc', 'Liferay': 'liferay-portal', 'CommCare HQ': 'commcare-hq', 'WordPress Gutenberg': 'gutenberg', 'PyTorch': 'pytorch', 'Kubernetes Test Infrastructure': 'test-infra', 'Keybase': 'client', 'Facebook React': 'react', 'Code.org': 'code-dot-org', 'Bitcoin Core': 'bitcoin', 'Arm Mbed OS': 'mbed-os', 'scikit-learn': 'scikit-learn', 'Nextcloud': 'server', 'Helm Charts': 'charts', 'Terraform': 'terraform', 'Ant Design': 'ant-design', 'Phalcon Framework Documentation': 'docs', 'Documentation for CMS Software for the Large Hadron Collider': 'cms-sw.github.io', 'Apache Kafka Mirror': 'kafka', 'Electron': 'electron', 'Zephyr Project': 'zephyr', 'The web-platform-tests Project': 'wpt', 'Marlin Firmware': 'Marlin', 'Apache MXNet': 'incubator-mxnet', 'Apache Beam': 'beam', 'Fastlane': 'fastlane', 'Kubernetes Website and Documentation': 'website', 'Ruby on Rails': 'rails', 'Zulip': 'zulip', 'Laravel': 'framework', 'Baidu PaddlePaddle': 'Paddle', 'Gatsby': 'gatsby', 'Rust Crate Registry': 'crates.io-index', 'Nintendo 3DS Custom Firmware': 'Guide_3DS', 'TiDB': 'tidb', 'Angular CLI': 'angular-cli', 'MAPS.ME': 'omim', 'Eclipse Che': 'che', 'Brave Browser': 'browser-laptop', 'Patchwork': 'patchwork', 'Angular Material': 'components', 'Python': 'cpython', 'Cataclysm: Dark Days Ahead': 'Cataclysm-DDA', 'Material-UI': 'material-ui', 'Ionic': 'ionic', 'Oppia': 'oppia', 'Alluxio': 'alluxio', 'XX Net': 'XX-Net', 'Microsoft .NET CLI': 'cli'}
reference_list = ['kubernetes', 'spark', 'vscode', 'nixpkgs', 'rust', 'blocklist-ipsets', 'origin', 'ansible', 'wp-calypso', 'corefx', 'roslyn', 'node', 'tensorflow', 'freeCodeCamp', 'tgstation', 'swift', 'elasticsearch', 'moby', 'cockroach', 'tweakCompatible', 'servo', 'flutter', 'homebrew-core', 'home-assistant', 'coreclr', 'Specs', 'kibana', 'julia', 'TypeScript', 'joomla-cms', 'DefiniteTyped', 'homebrew-cask', 'ceph', 'go', 'amphtml', 'edx-platform', 'pandas', 'istio', 'manageiq', 'godot', 'gentoo', 'odoo', 'azure-docs', 'magento2', 'salt', 'AdguardFilters', 'symfony', 'cmssw', 'openshift-ansible', 'core', 'grpc', 'liferay-portal', 'commcare-hq', 'gutenberg', 'pytorch', 'test-infra', 'client', 'react', 'code-dot-org', 'bitcoin', 'mbed-os', 'scikit-learn', 'server', 'charts', 'terraform', 'ant-design', 'docs', 'cms-sw.github.io', 'kafka', 'electron', 'zephyr', 'wpt', 'Marlin', 'incubator-mxnet', 'beam', 'fastlane', 'website', 'rails', 'zulip', 'framework', 'Paddle', 'gatsby', 'crates.io-index', 'Guide_3DS', 'tidb', 'angular-cli', 'omim', 'che', 'browser-laptop', 'patchwork', 'components', 'cpython', 'vgstation13', 'Cataclysm-DDA', 'material-ui', 'ionic', 'oppia', 'alluxio', 'XX-Net', 'cli']




#gui
window = tk.Tk()
window.title('VysotskiyD.V.')
window.geometry('600x300')
window.resizable(height=False, width=False)


preview = Label(window, text='Practice-12')
preview.place(x = 5, y = 0)


entry = Entry(window, width=30)
entry.place(x = 5, y = 25)


button = Button(window, text='scrape', command=scrape)
button.place(x = 190, y = 22)


preview = Label(window, text='Scrape output:')
preview.place(x = 5, y = 50)


text = scrolledtext.ScrolledText(window, width=60, height=14, bg='white', fg='black')
text.place(x = 5, y = 70)


window.mainloop()