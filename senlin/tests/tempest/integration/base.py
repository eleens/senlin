#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tempest import config

from senlin.tests.tempest import base
from senlin.tests.tempest.common import clustering_client
from senlin.tests.tempest.common import compute_client
from senlin.tests.tempest.common import messaging_client
from senlin.tests.tempest.common import network_client

CONF = config.CONF


class BaseSenlinIntegrationTest(base.BaseSenlinTest):

    credentials = ['admin']

    @classmethod
    def setup_clients(cls):
        super(BaseSenlinIntegrationTest, cls).setup_clients()
        cls.client = clustering_client.ClusteringIntegrationClient(
            cls.os_admin.auth_provider,
            CONF.clustering.catalog_type,
            CONF.identity.region,
            **cls.default_params_with_timeout_values
        )

        cls.messaging_client = messaging_client.V2MessagingClient(
            cls.os_admin.auth_provider,
            CONF.messaging.catalog_type,
            CONF.identity.region,
            **cls.default_params_with_timeout_values
        )


class BaseSenlinIntegrationNonAdminTest(base.BaseSenlinTest):

    @classmethod
    def setup_clients(cls):
        super(BaseSenlinIntegrationNonAdminTest, cls).setup_clients()
        cls.client = clustering_client.ClusteringIntegrationClient(
            cls.os_primary.auth_provider,
            CONF.clustering.catalog_type,
            CONF.identity.region,
            **cls.default_params_with_timeout_values
        )

        cls.messaging_client = messaging_client.V2MessagingClient(
            cls.os_primary.auth_provider,
            CONF.messaging.catalog_type,
            CONF.identity.region,
            **cls.default_params_with_timeout_values
        )

        cls.compute_client = compute_client.V21ComputeClient(
            cls.os_primary.auth_provider,
            CONF.compute.catalog_type,
            CONF.identity.region,
            **cls.default_params_with_timeout_values
        )

        cls.network_client = network_client.NetworkClient(
            cls.os_primary.auth_provider,
            CONF.network.catalog_type,
            CONF.identity.region,
            **cls.default_params_with_timeout_values
        )
