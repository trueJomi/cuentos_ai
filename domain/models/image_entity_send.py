class SendQueryIamgeEntity:
    
    def __init__(self, prompt):
        self.prompt = prompt
    
    def to_dict(self):
        rest_message = {
            "prompt": f"{self.prompt}, perfect face, master piece",
            "negative_prompt":"bad-hands-5, bad-image-v2-39000 , NSFW",
            "styles":[
                "string"
            ],
            "seed":-1,
            "subseed":-1,
            "subseed_strength":0.8,
            "seed_resize_from_h":-1,
            "seed_resize_from_w":-1,
            "sampler_name":"DPM++ 2M Karras",
            "batch_size":1,
            "n_iter":1,
            "steps":20,
            "cfg_scale":7.5,
            "width":512,
            "height":512,
            "restore_faces": True,
            "tiling": False,
            "do_not_save_samples": False,
            "do_not_save_grid": False,
            "eta":0.0,
            "denoising_strength":0.0,
            "s_min_uncond":0.0,
            "s_churn":0.0,
            "s_tmax":0.0,
            "s_tmin":0.0,
            "s_noise":0.0,
            "override_settings":{
                
            },
            "override_settings_restore_afterwards": True,
            "refiner_checkpoint":"cuteyukimixAdorable_midchapter2",
            "refiner_switch_at":0.0,
            "disable_extra_networks": False,
            "comments":{
                
            },
            "enable_hr": False,
            "firstphase_width":0,
            "firstphase_height":0,
            "hr_scale":1,
            "hr_upscaler":"string",
            "hr_second_pass_steps":0,
            "hr_resize_x":0,
            "hr_resize_y":0,
            "hr_checkpoint_name":"",
            "hr_sampler_name":"",
            "hr_prompt":"",
            "hr_negative_prompt":"",
            "sampler_index":"",
            "script_name": "",
            "script_args":[
                
            ],
            "send_images": True,
            "save_images": False,
            "alwayson_scripts":{
                
            }
        }
        return rest_message