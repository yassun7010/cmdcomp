---
title: Overview
---

## Config

Cmdcomp automatically generates a completion file according to the contents of
the configuration file.

The overall structure of the configuration file is shown below.

```yaml
cmdcomp:
  version: "2"
app:
  {{ App }}
root:
  {{ Command }}
```

More detailed information is given in the next section.

Please refer to
[JSON Schema](https://raw.githubusercontent.com/yassun7010/cmdcomp/main/docs/config.schema.json)
for exact schema information.
