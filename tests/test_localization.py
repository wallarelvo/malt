
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import malt
# import math


def test_evolving():
    sim = malt.Simulation(
        x_dim=100,
        y_dim=100,
        randomly_generate=True,
        num_nodes=10,
        time_noise=2,
        # intensity_noise=0.1,
        scene="scenes/s-1.out",
        confidence_noise=0.1
    )
    dr = malt.Drawer(sim.x_dim, sim.y_dim)
    dr.draw_risk_grid(sim.scene).update()

    r_ref = 1
    l_ref = 100
    src_x = 30
    src_y = 80

    for i in xrange(200):
        local_instance = sim.step(src_x, src_y, r_ref, l_ref)
        dr.draw_nodes(local_instance.sim.node_positions)

        # res = local_instance.get_locations()
        dr.draw_source(
            local_instance.get_max_location().get_position(),
            (1, 1, 1), -2
        )

        dr.draw_source(malt.Point(src_x, src_y), (0, 1, 0), -3)

        dr.update()
        dr.clear_all()

        # print "Locations:", res
        print local_instance.get_error()

        # local_instance.plot()

if __name__ == "__main__":
    test_evolving()
