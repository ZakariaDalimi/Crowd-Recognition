import math

class Tracker:
    def __init__(self):
        # Store the center positions of the objects
        self.center_points = {}
        # Keep the count of the IDs
        # each time a new object id detected, the count will increase by one
        self.id_count = 1

    def update(self, objects_rect):
        # Objects boxes and ids
        objects_bbs_ids = []

        # Get center point of new object
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Find out if that object was detected already
            match_found = False
            for object_id, center in self.center_points.items():
                dist = math.hypot(cx - center[0], cy - center[1])

                if dist < 35:
                    objects_bbs_ids.append([x, y, w, h, object_id])
                    match_found = True
                    break

            # New object is detected, assign a new ID to that object
            if not match_found:
                object_id = self.id_count
                self.center_points[object_id] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, object_id])
                self.id_count += 1

        # Remove old IDs from center_points
        self.center_points = {obj_id: center for obj_id, center in self.center_points.items() if obj_id in [bb_id for _, _, _, _, bb_id in objects_bbs_ids]}

        return objects_bbs_ids
