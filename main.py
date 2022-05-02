'''
- It use to make folder hierarchy and save to JSON format.
- It also counts number of files based on file extension.
'''

'''
MIT License

Copyright (c) 2022 Kartavya Patel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import json, os, re

class counter:
    def __init__(self, path=None, save_on_that_path=False) -> None:
        self.__path = os.getcwd() if path==None else path
        self.__dictionary = None
        self.__total_files_count = {}
        self.save_on_path = save_on_that_path
    
    def recursion(self, path):
        try:
            dictionary = {}
            for item in os.listdir(path):
                if os.path.isfile(f'{path}/{item}'):
                    ext = item.split('.')
                    if len(ext)==1:
                        try:
                            dictionary['undefined_extension']+=1
                        except:
                            dictionary['undefined_extension']=1
                        
                        if 'undefined_extension' in self.__total_files_count:
                            self.__total_files_count['undefined_extension']+=1
                        if not 'undefined_extension' in self.__total_files_count:
                            self.__total_files_count['undefined_extension']=1

                    else:
                        ext = ext[-1].lower()
                        try:
                            dictionary[ext]+=1
                        except:
                            dictionary[ext]=1
                        
                        if ext in self.__total_files_count:
                            self.__total_files_count[ext]+=1
                        if not ext in self.__total_files_count:
                            self.__total_files_count[ext]=1

                if os.path.isdir(f'{path}/{item}'):
                    dictionary[item]=self.recursion(f'{path}/{item}')
            return dictionary
        except:
            pass

    def save_json(self):
        output = {self.__path:self.recursion(self.__path)}

        self.__total_files_count = {item:self.__total_files_count[item] for item in sorted(self.__total_files_count, key=lambda x: self.__total_files_count[x], reverse=True)}

        for item in self.__total_files_count:
            output[item] = self.__total_files_count[item]

        if self.save_on_path==True:
            save_type = f'{self.__path}/folder_hierarchy.json'
        if self.save_on_path==False:
            save_type = self.__path.replace("/","_").replace(":","_").replace("\\","_").replace('.',"_")
            save_type = f'{save_type}_folder_hierarchy.json'
            regex = re.compile(r'[_]{2,}')

            while len(regex.findall(save_type))!=0:
                for underscores in regex.findall(save_type):
                    save_type = save_type.replace(underscores, '_')
            print(save_type)

        with open(save_type,'w',encoding='utf-8') as file:
            file.write(json.dumps(output, indent=4))

        print(f'Saved as {save_type}')

obj = counter('./')

obj.save_json()