from flask import Flask
from uwsgidecorators import postfork

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from src.Config.Container import Container
from src.Config.Dependency import Dependency
from src.Driver.QuotationAction import quotation_action

app = Flask(__name__)

instrumentor = FlaskInstrumentor()
instrumentor.instrument_app(app)
tracer = trace.get_tracer(__name__)

@postfork
def init_tracing():
    resource = Resource.create(attributes={"service.name": "catle-quotation"})

    trace.set_tracer_provider(TracerProvider(resource=resource))
    # This uses insecure connection for the purpose of example. Please see the
    # OTLP Exporter documentation for other options.
    span_processor = BatchSpanProcessor(
        OTLPSpanExporter(endpoint="http://signoz:4317", insecure=True)
    )
    trace.get_tracer_provider().add_span_processor(span_processor)



container = Container()
Dependency.register_default(container=container)

@app.route('/collectQuotation')
def collect_quotation():
 return quotation_action(container=container)


if __name__ == "__main__":
    app.run()