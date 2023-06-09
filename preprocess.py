# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""
    preprocess
"""
import os
from src.utils.args import get_args
from src.dataset.cyclegan_dataset import create_dataset

if __name__ == '__main__':
    args = get_args("predict")
    result_path = args.outputs_dir
    ds_val = create_dataset(args)
    img_path = os.path.join(result_path, "00_data")
    os.makedirs(img_path)
    for i, data in enumerate(ds_val.create_dict_iterator(output_numpy=True)):
        file_name = "CycleGAN_data_bs" + str(args.batch_size) + "_" + str(i) + ".bin"
        file_path = img_path + "/" + file_name
        data['image'].tofile(file_path)
    print("=" * 20, "export bin files finished", "=" * 20)
