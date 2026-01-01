
from utils.simulate import run
import utils.params  as params
if __name__ == "__main__":
   
   
    input_parameters = params.get_from_json('params.input.json')
    simulated_params = run(input_parameters, shuffle=False, 
                           batch_processing=True,  parallel=8)
    params.save_params_to_file(simulated_params, 
                               f"params.simulated.json")
    print("Results Generated successfully!")

