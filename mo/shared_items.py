

def realesrgan_models_names():
    import mo.realesrgan_model
    return [x.name for x in mo.realesrgan_model.get_realesrgan_models(None)]


def postprocessing_scripts():
    import mo.scripts

    return mo.scripts.scripts_postproc.scripts


def sd_vae_items():
    import mo.sd_vae

    return ["Automatic", "None"] + list(mo.sd_vae.vae_dict)


def refresh_vae_list():
    import mo.sd_vae

    mo.sd_vae.refresh_vae_list()


def cross_attention_optimizations():
    import mo.sd_hijack

    return ["Automatic"] + [x.title() for x in mo.sd_hijack.optimizers] + ["None"]


def sd_unet_items():
    import mo.sd_unet

    return ["Automatic"] + [x.label for x in mo.sd_unet.unet_options] + ["None"]


def refresh_unet_list():
    import mo.sd_unet

    mo.sd_unet.list_unets()


ui_reorder_categories_builtin_items = [
    "inpaint",
    "sampler",
    "checkboxes",
    "hires_fix",
    "dimensions",
    "cfg",
    "seed",
    "batch",
    "override_settings",
]


def ui_reorder_categories():
    from mo import scripts

    yield from ui_reorder_categories_builtin_items

    sections = {}
    for script in scripts.scripts_txt2img.scripts + scripts.scripts_img2img.scripts:
        if isinstance(script.section, str):
            sections[script.section] = 1

    yield from sections

    yield "scripts"
