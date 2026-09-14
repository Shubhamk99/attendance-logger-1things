import re
import sys

SRC = "/private/tmp/claude-502/-Users-Shared-Personal-AI-projects/23b65ae2-b190-41a7-afb6-a7f9a8d0d8e5/scratchpad/connecto_jadx/sources/com/neosoft/connecto/network/ApiService.java"
OUT = "/Users/Shared/Personal/AI-projects/connecto-auth-probe/API_DOCUMENTATION.md"

HTTP_ANN_RE = re.compile(r'@(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)\("([^"]*)"\)')
METHOD_LINE_RE = re.compile(r'^\s*(Call<.+?>|Object)\s+(\w+)\((.*)\);\s*$')

with open(SRC, "r", encoding="utf-8") as f:
    lines = f.readlines()

def split_params(param_str):
    parts = []
    depth = 0
    current = ""
    for ch in param_str:
        if ch in "<(":
            depth += 1
        elif ch in ">)":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(current.strip())
            current = ""
        else:
            current += ch
    if current.strip():
        parts.append(current.strip())
    return parts

PARAM_ANN_RE = re.compile(r'@(Field|Query|Header|Path|Part|Body)(\(([^)]*)\))?\s+(.*)')

def parse_param(p):
    m = PARAM_ANN_RE.match(p)
    if m:
        kind = m.group(1)
        key_raw = m.group(3)
        rest = m.group(4).strip()
        type_and_name = rest.rsplit(" ", 1)
        ptype = type_and_name[0].strip() if len(type_and_name) == 2 else ""
        pname = type_and_name[1].strip() if len(type_and_name) == 2 else rest
        if key_raw is None:
            label = kind
        elif key_raw.startswith('"') and key_raw.endswith('"'):
            label = f"{kind}({key_raw})"
        else:
            label = f"{kind}({key_raw})"
        return {"kind": label, "type": ptype, "name": pname}
    else:
        type_and_name = p.rsplit(" ", 1)
        ptype = type_and_name[0].strip() if len(type_and_name) == 2 else ""
        pname = type_and_name[1].strip() if len(type_and_name) == 2 else p
        return {"kind": "", "type": ptype, "name": pname}

endpoints = []
i = 0
n = len(lines)
while i < n:
    m = HTTP_ANN_RE.search(lines[i])
    if m:
        http_method = m.group(1)
        path = m.group(2)
        modifiers = []
        j = i - 1
        while j >= 0:
            stripped = lines[j].strip()
            if stripped.startswith("@FormUrlEncoded") or stripped.startswith("@Multipart") or stripped.startswith("@Streaming"):
                modifiers.append(stripped.replace("@", ""))
                j -= 1
            else:
                break
        modifiers.reverse()

        k = i + 1
        method_line = None
        while k < n and k < i + 6:
            s = lines[k].strip()
            if s.startswith("@FormUrlEncoded") or s.startswith("@Multipart") or s.startswith("@Streaming"):
                modifiers.append(s.replace("@", ""))
                k += 1
                continue
            if s.startswith("@"):
                k += 1
                continue
            mm = METHOD_LINE_RE.match(lines[k])
            if mm:
                method_line = mm
            break

        if method_line:
            return_type = method_line.group(1)
            method_name = method_line.group(2)
            params_raw = method_line.group(3)
            params = [parse_param(p) for p in split_params(params_raw)] if params_raw.strip() else []
            resp_match = re.search(r'Call<(.+)>', return_type)
            response_type = resp_match.group(1) if resp_match else return_type
            endpoints.append({
                "http_method": http_method,
                "path": path,
                "modifiers": modifiers,
                "method_name": method_name,
                "response_type": response_type,
                "params": params,
            })
    i += 1

print(f"Parsed {len(endpoints)} endpoints", file=sys.stderr)

endpoints.sort(key=lambda e: (e["path"], e["http_method"]))

with open(OUT, "w", encoding="utf-8") as out:
    out.write("# Connecto API Documentation\n\n")
    out.write(f"Total endpoints: {len(endpoints)}\n\n")
    out.write("Interface: `com.neosoft.connecto.network.ApiService`\n\n")
    out.write("Base URLs (selected per-request by which Retrofit client instance is used):\n\n")
    out.write("| Client | Production base URL | Dev/staging base URL |\n")
    out.write("|---|---|---|\n")
    out.write("| Main app | `https://connecto.neosofttech.com/public/` | `https://connecto.php-dev.in/connecto/public/` |\n")
    out.write("| Knowledge base | `http://services.neosofttech.in/connect-to/` | - |\n")
    out.write("| CRM/Campaign | `https://crm.neosofttech.com/api/manage/` | `http://betacrm.neosofttech.com:3020/api/manage/` |\n")
    out.write("| Collab/SSO | `https://sso.neosofttech.com/sso-todos/` | (empty) |\n")
    out.write("| Support Tickets | `https://tickets.neosofttech.com/api/` | `https://neoticketportal.php-dev.in/api/` |\n")
    out.write("| RAB | `https://employee.neosofttech.com/` | `https://assessment.neosofttech.com/employee/` |\n\n")
    out.write("---\n\n")

    for e in endpoints:
        mods = f" [{', '.join(e['modifiers'])}]" if e["modifiers"] else ""
        out.write(f"## {e['http_method']} `{e['path']}`{mods}\n\n")
        out.write(f"- Method: `{e['method_name']}`\n")
        out.write(f"- Response: `{e['response_type']}`\n")
        if e["params"]:
            out.write("- Parameters:\n\n")
            out.write("| Annotation | Type | Name |\n")
            out.write("|---|---|---|\n")
            for p in e["params"]:
                out.write(f"| {p['kind']} | `{p['type']}` | `{p['name']}` |\n")
        else:
            out.write("- Parameters: none\n")
        out.write("\n")

print(f"Wrote {OUT}", file=sys.stderr)
