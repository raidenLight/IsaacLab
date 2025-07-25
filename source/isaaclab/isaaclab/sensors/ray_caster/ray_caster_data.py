# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import torch
from dataclasses import dataclass


@dataclass
class RayCasterData:
    """Data container for the ray-cast sensor."""

    pos_w: torch.Tensor = None
    """Position of the sensor origin in world frame.

    Shape is (N, 3), where N is the number of sensors.
    """
    quat_w: torch.Tensor = None
    """Orientation of the sensor origin in quaternion (w, x, y, z) in world frame.

    Shape is (N, 4), where N is the number of sensors.
    """
    ray_hits_w: torch.Tensor = None
    """The ray hit positions in the world frame.

    Shape is (N, B, 3), where N is the number of sensors, B is the number of rays
    in the scan pattern per sensor.
    """
    ray_distance: torch.Tensor | None = None
    """Distances (in meters) of the rays until they hit a target mesh.
    
    This distance is clipped to the maximum distance specified through
    :attr:`RayCasterCfg.max_distance`.

    Shape is (N, B), where N is the number of sensors, B is the number of rays
    in the scan pattern per sensor.

    Note:
        If the :attr:`RayCasterCfg.track_ray_distance` is False, then this quantity is None.
    """
