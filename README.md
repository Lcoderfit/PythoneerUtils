# PythoneerUtils
[![GitHub Super-Linter](https://github.com/Lcoderfit/PythoneerUtils/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)

Pythoneers实用工具


## 一、配置Super Linter自动代码检查工具
### 1.1 创建super linter配置文件
* 在项目根目录下创建.github/workflow/linter.yml文件

* linter.yml配置如下，注意：第一行的“\”是用于对"---"进行转译的(否则markdown格式会错乱)，正确的yaml文件不应该带有这个"\"
    ```text
    \---
    #################################
    #################################
    ## Super Linter GitHub Actions ##
    #################################
    #################################
    name: Lint Code Base
    
    #
    # Documentation: Github Actions工作流中文文档参考下方链接
    # https://docs.github.com/cn/actions/reference/workflow-syntax-for-github-actions
    #
    
    #############################
    # Start the job on all push #
    #############################
    on:
      push:
      	# 表示当直接push代码到main,dev,release-*分支时会触发事件
      	# release-*后面的"*"是通配符
      	# 如果要指定直接push代码到某些分支时不触发事件，则用branches-ignore: [branch_name]
        branches: [main, dev, release-*]
      pull_request:
        # 表示当对main，dev，release-*分支创建一个pull request时会触发事件
        branches: [main, dev, release-*]
    
    ###############
    # Set the Job #
    ###############
    jobs:
      build:
        # 任务名
        name: Lint Code Base
        # 任务运行的环境
        runs-on: ubuntu-latest
    
        ##################
        # Load all steps #
        ##################
        steps:
          ##########################
          # Checkout the code base #
          ##########################
          - name: Checkout Code
            uses: actions/checkout@v2
            with:
              # Full git history is needed to get
              # a proper list of changed files within `super-linter`
              fetch-depth: 0
    
          ################################
          # Run Linter against code base #
          ################################
          - name: Lint Code Base
            uses: github/super-linter@v3
            env:
              # 如果为false，表示只对修改的文件进行检查，否则对所有文件进行检查
              VALIDATE_ALL_CODEBASE: false
              # false表示不对yaml文件进行语法检查
              VALIDATE_YAML: false
              # 默认分支
              DEFAULT_BRANCH: main
              GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    ```
    
    

### 1.2 在Linux环境中手动对linter.yml进行语法检查

* 下载yamllint

  ```text
  $sudo apt-get install yamllint
  ```

* 由于Super-Linter对yaml文件进行检查的时候老是会报错（wrong new line character: expected），暂时无法解决，所以通过在linter.yml文件添加 VALIDATE_YAML: false 让Super-Linter不对linter.yml进行检查，转而采用手动检查的方法。

  ```text
  $yamllint .github/workflow/linter.yml
  如果输出如下，则vim编辑linter.yml,将文件最后一行末尾的换行删除即可。
  
  .github/workflows/linter.yml
    2:2       warning  missing starting space in comment  (comments)
    3:2       warning  missing starting space in comment  (comments)
    4:2       warning  missing starting space in comment  (comments)
    5:2       warning  missing starting space in comment  (comments)
    6:2       warning  missing starting space in comment  (comments)
    14:2      warning  missing starting space in comment  (comments)
    16:2      warning  missing starting space in comment  (comments)
    24:2      warning  missing starting space in comment  (comments)
    26:2      warning  missing starting space in comment  (comments)
    34:6      warning  missing starting space in comment  (comments)
    36:6      warning  missing starting space in comment  (comments)
    38:8      warning  missing starting space in comment  (comments)
    40:8      warning  missing starting space in comment  (comments)
    48:8      warning  missing starting space in comment  (comments)
    50:8      warning  missing starting space in comment  (comments)
    57:52     error    no new line character at the end of file  (new-line-at-end-of-file)
  ```

  

  