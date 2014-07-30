def from_params_or_json(req, field):
    return req.params.get(field) or (req.json.get(field) if req.json else '')
