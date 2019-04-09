import _plotly_utils.basevalidators


class TickformatValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='tickformat',
        parent_name='layout.scene.yaxis',
        **kwargs
    ):
        super(TickformatValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'plot'),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )