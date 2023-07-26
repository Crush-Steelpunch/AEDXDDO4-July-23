# Hugo Challenge

1. On Go2MyPC, download hugo from <https://github.com/gohugoio/hugo/releases/download/v0.115.4/hugo_0.115.4_windows-amd64.zip>
2. unzip the file
3. Open GitBash and run
```bash
cd
mkdir bin
```
4. In Explorer copy the `hugo.exe` from the extracted folder to `C:\Users\Admin\bin`
5. Create a new repo for your hugo site in Github (maybe call it hugo-site)
6. `git clone` the repo to your go2mypc
7. `cd` into the repo folder and run the following:
```bash
hugo new site .
git add .
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
echo "theme = 'ananke'" >> hugo.toml
git commit -m "Initial Commit"
```
8. Follow the instructions from this step <https://gohugo.io/getting-started/quick-start/#add-content>
9. change any draft pages to `False`
10. Push to Github
11. Follow these instuctions <https://gohugo.io/hosting-and-deployment/hosting-on-github/> to create the github pages and github actions.
12. go wild with markdown and make a page to be proud of
