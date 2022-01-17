# Copyright 2021 The Couler Authors. All rights reserved.
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

from collections import OrderedDict


class Volume(object):
    def __init__(self, name, claim_name=None, config_map=None):
        self.name = name
        self.claim_name = claim_name
        self.config_map = config_map

    def to_dict(self):
        if self.claim_name is not None:
            return OrderedDict(
                {
                    "name": self.name,
                    "persistentVolumeClaim": {"claimName": self.claim_name},
                }
            )
        elif self.config_map is not None:
            return OrderedDict(
                {
                    "name": self.name,
                    "configMap": {"name": self.config_map,
                                  "defaultMode": "0777"},
                }
            )



class VolumeMount(object):
    def __init__(self, name, mount_path, sub_path=None):
        self.name = name
        self.mount_path = mount_path
        self.sub_path = None

    def to_dict(self):
        if self.sub_path is not None:
            return OrderedDict({"name": self.name,
                                "mountPath": self.mount_path,
                                "subPath": self.sub_path})
        else:
            return OrderedDict({"name": self.name,
                                "mountPath": self.mount_path})
