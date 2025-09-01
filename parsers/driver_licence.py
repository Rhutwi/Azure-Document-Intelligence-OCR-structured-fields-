def parse(result) -> (dict, float):
    # heuristic extraction (works for layout/custom)
    fields = {}
    conf = 0.0
    if result.documents:
        d = result.documents[0]
        for f in d.fields:
            fields[f] = getattr(d.fields[f], "content", None)
        conf = getattr(d, "confidence", 0.9) or 0.9
    else:
        # fallback: dig from key-values/tables
        for kv in getattr(result, "key_value_pairs", []):
            k = getattr(kv.key, "content", "").lower()
            v = getattr(kv.value, "content", "")
            if "licence" in k and "number" in k: fields["lic_no"] = v
            if "name" in k: fields.setdefault("name", v)
            if "expiry" in k or "exp" in k: fields["expiry"] = v
        conf = 0.7
    return fields, conf
