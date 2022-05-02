# Folder Tree
<div style="width: 100%;text-align: center;">
    <div title="patelka2211/Folder-Tree on GitHub" style="display: flex;flex-direction: column;align-items: center;justify-content: space-around; max-width: 100vw; margin: auto; padding: 0.6vh;border: 1px solid #b9bbbe99; border-radius: 1.6vh;">
        <img src="https://opengraph.githubassets.com/1fjljefe/patelka2211/Folder-Tree" alt="" style="width: 100%;height: 100%;border-radius: 1vh;">
        <div style="margin: 5px auto;color: #58a6ff;">
            github.com /
            <code>
            <a href="https://github.com/patelka2211/Folder-Tree" title="patelka2211/Folder-Tree on GitHub" target="blank_" style="cursor: pointer;">
                <a href="https://github.com/patelka2211" title="patelka2211 on GitHub" style="text-decoration: none;color: #58a6ff;" target="blank_">patelka2211</a> / <a href="https://github.com/patelka2211/Folder-Tree" title="patelka2211/Folder-Tree on GitHub" style="text-decoration: none;color: #58a6ff;" target="blank_">Folder-Tree</a>
            </a>
        </code>
        </div>
    </div>
</div>

---
# Description
It lets you see folder in a hierarchical manner and also counts every file extensions present in that folder.

- It use to make folder hierarchy and save to JSON format.
- It also counts number of files based on file extension.

# Examples

[Hierarchy JSON file of this folder](./_folder_hierarchy.json)

[Hierarchy JSON file of "Folder1"](./_Folder1_folder_hierarchy.json)

```json
// Example
{
    "root_folder":{
        "sub_folder1":{
            "nested_folder":{
                "c": 2
            },
            "py": 5,
            "html": 3
        },
        "sub_folder2":{
            "js": 4
        },
        "html": 2
    },
    "c": 2,
    "py": 5,
    "html": 5,
    "js": 4
}
```

# License
[MIT License](./LICENSE)

Copyright (c) 2022 [Kartavya Patel](https://github.com/patelka2211)