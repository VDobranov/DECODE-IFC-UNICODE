если компилить через «flet publish»:
```bash
flet publish main.py --route-url-strategy hash --base-url {имя репозитория}
```

кроме того, в static.yml от Github Workflows должно быть указано:
```yml
uses: actions/upload-pages-artifact@v3
with:
  path: './dist/'
```