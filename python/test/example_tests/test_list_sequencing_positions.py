from pathlib import Path
import subprocess
import sys

from minknow_api import manager_pb2

from test_minknow_server import ManagerTestServer

list_positions_source = (
    Path(__file__).parent.parent.parent
    / "minknow_api"
    / "examples"
    / "list_sequencing_positions.py"
)


def normalize_new_lines(val):
    return val.replace("\r\n", "\n").replace("\r", "\n")


def test_list_sequencing_positions_no_positions():
    """Verify no positions are listed when nothing available."""

    with ManagerTestServer() as server:
        p = subprocess.run(
            [sys.executable, str(list_positions_source), "--port", str(server.port)],
            check=True,
            stdout=subprocess.PIPE,
        )

        expected_output = (
            """Available sequencing positions on localhost:%s:
"""
            % server.port
        )

        assert normalize_new_lines(p.stdout.decode("utf-8")) == normalize_new_lines(
            expected_output
        )


def test_list_sequencing_positions_gridion_positions():
    """Verify gridion positions are listed as expected."""
    test_positions = [
        manager_pb2.FlowCellPosition(
            name="X1",
            state=manager_pb2.FlowCellPosition.State.STATE_RUNNING,
            rpc_ports=manager_pb2.FlowCellPosition.RpcPorts(secure=8000),
        ),
        manager_pb2.FlowCellPosition(
            name="X2",
            state=manager_pb2.FlowCellPosition.State.STATE_RUNNING,
            rpc_ports=manager_pb2.FlowCellPosition.RpcPorts(secure=8001),
        ),
        manager_pb2.FlowCellPosition(
            name="X3",
            state=manager_pb2.FlowCellPosition.State.STATE_RUNNING,
            rpc_ports=manager_pb2.FlowCellPosition.RpcPorts(secure=8002),
        ),
        manager_pb2.FlowCellPosition(
            name="X4",
            state=manager_pb2.FlowCellPosition.State.STATE_RUNNING,
            rpc_ports=manager_pb2.FlowCellPosition.RpcPorts(secure=8003),
        ),
        manager_pb2.FlowCellPosition(
            name="X5", state=manager_pb2.FlowCellPosition.State.STATE_INITIALISING
        ),
    ]

    with ManagerTestServer(positions=test_positions) as server:
        p = subprocess.run(
            [sys.executable, str(list_positions_source), "--port", str(server.port)],
            check=False,
            stdout=subprocess.PIPE,
        )

        expected_output = (
            """Available sequencing positions on localhost:%s:
X1: running
  secure: 8000
X2: running
  secure: 8001
X3: running
  secure: 8002
X4: running
  secure: 8003
X5: initialising
"""
            % server.port
        )

        assert normalize_new_lines(p.stdout.decode("utf-8")) == normalize_new_lines(
            expected_output
        )
