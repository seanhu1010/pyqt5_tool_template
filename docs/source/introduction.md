Introduction
=============

# 1. 项目简介

测试工程模板项目

### **功能**

*

### **使用**
```shell
pip install -r requirements.txt
```

# 2. 工程文件结构
```shell
TBD
```

# 3. 编码规范
* 遵循[Google Python Style Guide](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules.html)  和[PEP8](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules.html)规范

* **包名**和**文件名**使用蛇形命名法

* **类**使用大驼峰命名法

* **函数**和**变量**使用小驼峰命名法

# 4. Docstrings

推荐使用[Google style](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings), PyCharm->Settings->Tools->Docstrings->Docstrings format选择Google, All of the following section headers are supported:

* Args (alias of Parameters)
* Arguments (alias of Parameters)
* Attention
* Attributes
* Caution
* Danger
* Error
* Example
* Examples
* Hint
* Important
* Keyword Args (alias of Keyword Arguments)
* Keyword Arguments
* Methods
* Note
* Notes
* Other Parameters
* Parameters
* Return (alias of Returns)
* Returns
* Raise (alias of Raises)
* Raises
* References
* See Also
* Tip
* Todo
* Warning
* Warnings (alias of Warning)
* Warn (alias of Warns)
* Warns
* Yield (alias of Yields)
* Yields

# 5. 提交说明

### 分支

* main分支为主分支（保护分支），不能直接在main上进行修改代码提交

* develop分支为测试分支，所有开发完成需要提交测试的功能合并到该分支

* feature分支为开发分支，大家根据不同需求创建独立的功能分支，开发完成后合并到develop分支

* fix分支为bug修复分支，需要根据实际情况对已发布的版本进行漏洞修复时使用该分支

### 审核制度

略

### Tag

采用三段式， v版本.里程碑.序号，如 v1.2.1

* 架构升级或架构重大调整，修改第1位

* 新功能上线或者模块大的调整，修改第2位

* bug修复上线，修改第3位

### Git提交信息

Commit Message一般包含三部分：Header，Body和Footer

#### Header

* type：用于说明commit的类别，规定为如下几种

* feat：新增功能；

* fix：bug修复；

* docs：修改文档；

* refactor：代码重构，未新增任何功能和修复bug；

* build：改变构建流程，新增依赖库，工具等；

* style：仅仅修改了空格、缩进等，不改变代码逻辑；

* perf：改善性能和体现的修改；

* chore：非src和test的修改；

* test：测试用例的修改；

* ci：自动化流程配置修改；

* revert：回滚到某个版本；

* scope：【可选】用于说明commit的影响范围

* subject：commit的简短说明，尽量简短

#### Body

* 本次commit的详细描述，可分多行

##### Footer

* 不兼容变动：需要描述相关信息；

* 关闭指定的Issue：输入Issue信息；
